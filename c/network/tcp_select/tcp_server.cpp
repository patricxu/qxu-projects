#include <iostream>
#include <string>
#include <unistd.h>
#include <stdio.h>
#include <sys/types.h>    
#include <sys/socket.h>    
#include <sys/un.h>    
#include <unistd.h>    
#include <stdlib.h>    
#include <errno.h>
#include <string.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netdb.h>
#include <map>
#include "Buff.h"

#define PORT "5189" // 我們正在 listen 的 port
#define MAXINT32 0x7fffffff
#define HEADER_SIZE 8
#define MAXPACKLEN (8192 + HEADER_SIZE)


typedef std::map<int, CBuff*> TSock2BufferMap;
typedef std::pair<int, CBuff*> TSock2BufferPair;
TSock2BufferMap g_mapSock2Buff;

int GetInt32Le(char* buf)
{
	int res = 0;
	res = buf[0] | (buf[1] << 8) | (buf[2] << 16) | (buf[3] << 24);
	return res;
}

void ToUpperLayer(char* buf, int len)
{
	printf("ToUpperLayer pakcet len = %d\n", len);
}

// 取得 sockaddr，IPv4 或 IPv6：
void *get_in_addr(struct sockaddr *sa)
{
	if (sa->sa_family == AF_INET) {
		return &(((struct sockaddr_in*)sa)->sin_addr);
	}

	return &(((struct sockaddr_in6*)sa)->sin6_addr);
}

#define PACK_ERROR -1
#define PACK_INCOMPLETE_HEADER 1
#define PACK_INCOMPLETE_PAYLOAD 2
#define PACK_COMPLETE 0
#define PACK_COMPLETE_REMAINS 3


// |---packetLen----|----padding----|---payload----------|
//     4 bytes           4 bytes        variable
// |---------------------packetLen bytes ----------------|

int OnDataAvailble(const int sock, CBuff* pBuf, const int nBytesAvail)
{
	static int s_packLen = 0;
	int nRecv = 0;
	
// 	printf("OnDataAvaialbe nBytesAvail=%d s_packLen=%d\n", nBytesAvail, s_packLen);
	if (s_packLen == 0 && nBytesAvail < HEADER_SIZE)
	{
		//incomplet header
		return PACK_INCOMPLETE_HEADER;
	}
	else
	{
		//complete headr
		if (s_packLen == 0)
		{
			//new packet
			//read header
			nRecv = recv(sock, pBuf->GetBuff(), HEADER_SIZE, 0);
			if (nRecv != HEADER_SIZE)
			{
				//should not be here
				printf("error in recv\n");
				s_packLen = 0;
				return PACK_ERROR;
			}

			//get total packLen
			s_packLen = GetInt32Le(pBuf->GetBuff()); 

			if (s_packLen > MAXPACKLEN || s_packLen < 0)
			{
				printf("The packet size excees the max number. \n", sock);
				s_packLen = 0;
				return PACK_ERROR;
			}

			//make sure the buffer is large enough
			if (pBuf->GetBuffSize() < s_packLen)
			{
				if(pBuf->Resize(s_packLen) == false)
				{
					printf("Resize buffer for socket %d failed\n", sock);
					return PACK_ERROR;
				}

				printf("Resize buffer for socket %d with size=%d\n", sock, s_packLen);
			}
		}

		int payloadLen = s_packLen - HEADER_SIZE;
		int nLeft = recv(sock, pBuf->GetBuff()+HEADER_SIZE, payloadLen, MSG_PEEK | MSG_DONTWAIT);
		if (payloadLen == nLeft)
		{
			//complete packet, no remains		
			//recv the payload
			nRecv = recv(sock, pBuf->GetBuff()+HEADER_SIZE, payloadLen, 0);
			if (nRecv != payloadLen)
			{
				printf("complete packet, no remains. But error in recv payload. payloadLen = %d nRecv = %d\n", sock, payloadLen, nRecv);
				s_packLen = 0;
				return PACK_ERROR;
			}
			
			ToUpperLayer(pBuf->GetBuff()+HEADER_SIZE, payloadLen);
			s_packLen = 0;
			return PACK_COMPLETE;
		}
		else if (payloadLen > nLeft)
		{
			//incomplete packet
			return PACK_INCOMPLETE_PAYLOAD;
		}
		else
		{
			//complete packet, but remains
			nRecv = recv(sock, pBuf->GetBuff()+HEADER_SIZE, payloadLen, 0);
			if (nRecv != payloadLen)
			{
				printf("complete packet, have remains. But error. payloadLen = %d, nRecv = %d nBytesAvail =%d\n", payloadLen, nRecv, nBytesAvail);
				s_packLen = 0;
				return PACK_ERROR;
			}

			ToUpperLayer(pBuf->GetBuff()+HEADER_SIZE, payloadLen);
			s_packLen = 0;
			return PACK_COMPLETE_REMAINS;
		}
	}
}

int server(void)
{
	fd_set master; // master file descriptor 清單
	fd_set read_fds; // 給 select() 用的暫時 file descriptor 清單
	int fdmax; // 最大的 file descriptor 數目

	int listener; // listening socket descriptor
	int newfd; // 新接受的 accept() socket descriptor
	struct sockaddr_storage remoteaddr; // client address
	socklen_t addrlen;

	int nbytes;

	char remoteIP[INET6_ADDRSTRLEN];

	int yes=1; // 供底下的 setsockopt() 設定 SO_REUSEADDR
	int i, j, rv;

	struct addrinfo hints, *ai, *p;

	FD_ZERO(&master); // 清除 master 與 temp sets
	FD_ZERO(&read_fds);

	// 給我們一個 socket，並且 bind 它
	memset(&hints, 0, sizeof hints);
	hints.ai_family = AF_UNSPEC;
	hints.ai_socktype = SOCK_STREAM;
	hints.ai_flags = AI_PASSIVE;

	if ((rv = getaddrinfo(NULL, PORT, &hints, &ai)) != 0) {
		fprintf(stderr, "selectserver: %s\n", gai_strerror(rv));
		exit(1);
	}

	for(p = ai; p != NULL; p = p->ai_next) {
		listener = socket(p->ai_family, p->ai_socktype, p->ai_protocol);
		if (listener < 0) {
			continue;
		}

		// 避開這個錯誤訊息："address already in use"
		setsockopt(listener, SOL_SOCKET, SO_REUSEADDR, &yes, sizeof(int));

		if (bind(listener, p->ai_addr, p->ai_addrlen) < 0) {
			close(listener);
			continue;
		}

		break;
	}

	// 若我們進入這個判斷式，則表示我們 bind() 失敗
	if (p == NULL) {
		fprintf(stderr, "selectserver: failed to bind\n");
		exit(2);
	}
	freeaddrinfo(ai); // all done with this

	// listen
	if (listen(listener, 10) == -1) {
		perror("listen");
		exit(3);
	}

	// 將 listener 新增到 master set
	FD_SET(listener, &master);

	// 持續追蹤最大的 file descriptor
	fdmax = listener; // 到此為止，就是它了

	// 主要迴圈
	for( ; ; ) {
		read_fds = master; // 複製 master

		if (select(fdmax+1, &read_fds, NULL, NULL, NULL) == -1) {
			perror("select");
			exit(4);
		}

		// 在現存的連線中尋找需要讀取的資料
		for(i = 0; i <= fdmax; i++) {
			if (FD_ISSET(i, &read_fds)) { // 我們找到一個！！
				if (i == listener) {
					// handle new connections
					addrlen = sizeof remoteaddr;
					newfd = accept(listener,
						(struct sockaddr *)&remoteaddr,
						&addrlen);

					if (newfd == -1) {
						perror("accept");
					} else {
						FD_SET(newfd, &master); // 新增到 master set
						if (newfd > fdmax) { // 持續追蹤最大的 fd
							fdmax = newfd;
						}
						printf("selectserver: new connection from %s on "
							"socket %d\n",
							inet_ntop(remoteaddr.ss_family,
							get_in_addr((struct sockaddr*)&remoteaddr),
							remoteIP, INET6_ADDRSTRLEN),
							newfd);

						//为sock创建缓冲区
						CBuff* pBuf = new CBuff;
						g_mapSock2Buff.insert(TSock2BufferPair(newfd, pBuf));
					}

				} else {
					//获取sock的缓冲区
					CBuff* pBuff = NULL;
					pBuff = g_mapSock2Buff[i];
					if (!pBuff)
					{
						//no buffer for the socket. something wrong. close the socket
						close(i);
						FD_CLR(i, &master);
						continue;
					}

					// 處理來自 client 的資料
					if ((nbytes = recv(i, pBuff->GetBuff(), pBuff->GetBuffSize(), MSG_PEEK | MSG_DONTWAIT)) <= 0) 
					{
						// got error or connection closed by client
						if (nbytes == 0) 
						{
							// 關閉連線
							printf("selectserver: socket %d hung up\n", i);
						} 
						else
						{
							perror("recv");
						}
						close(i); // bye!
						FD_CLR(i, &master); // 從 master set 中移除

						g_mapSock2Buff.erase(i);
						delete pBuff;
					} 
					else
					{
						//handle the data
						int res = OnDataAvailble(i, pBuff, nbytes);
						if (res == PACK_ERROR)
						{
							printf("corrupted packet! close socket %d\n", i);
							close(i);
							FD_CLR(i, &master);
							g_mapSock2Buff.erase(i);
							delete pBuff;
						}					
					}
				} // END handle data from client
			} // END got new incoming connection
		} // END looping through file descriptors
	} // END for( ; ; )--and you thought it would never end!
}

int main()
{
    server();
    return 0;
}
