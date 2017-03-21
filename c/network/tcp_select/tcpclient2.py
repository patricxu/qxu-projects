# Python Version:3.5.1
# Echo client program
import socket
import time
import pdb

HOST = '127.0.0.1'    # The remote host
PORT = 5188              # The same port as used by the server

g_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
g_sock.connect((HOST, PORT))

def comm():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b'Hello, world'+b'\x00')
#        data = s.recv(1024)
#    print('Received', repr(data))

def SendMsg2Speed(codes, fields):
    print("SendMsg2Speed {0} {1}", codes, fields)
    tmp = bytes(codes.encode("utf8")+b'\x00')
    print((len(tmp)+8).to_bytes(4, byteorder="little") + (0).to_bytes(4, byteorder="little") + tmp)
    g_sock.sendall((len(tmp)+8).to_bytes(4, byteorder="little") + (0).to_bytes(4, byteorder="little") + tmp)
#    g_sock.recv(1024)

def close():
    g_sock.close()



pdb.set_trace();
SendMsg2Speed("haha quxi", "fields")
SendMsg2Speed("haha1 quxi", "fields")
SendMsg2Speed("haha2 quxi", "fields")

"""
g_sock.sendall((3+8).to_bytes(4, byteorder="little"))
g_sock.sendall((0).to_bytes(4, byteorder="little"))
g_sock.sendall(bytes(1))
g_sock.sendall(bytes(2))

g_sock.sendall((100000+8).to_bytes(4, byteorder="little"))
g_sock.sendall((0).to_bytes(4, byteorder="little"))
g_sock.sendall(bytes(100000))
"""
g_sock.sendall((100+8).to_bytes(4, byteorder="little"))
g_sock.sendall((0).to_bytes(104, byteorder="little"))

g_sock.close()
#comm()
