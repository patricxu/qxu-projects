# Python Version:3.5.1
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

def close():
    g_sock.close()


pdb.set_trace();
"""
#分包发送
g_sock.sendall((3+8).to_bytes(4, byteorder="little"))
g_sock.sendall((0).to_bytes(4, byteorder="little"))
g_sock.sendall(bytes(1))
g_sock.sendall(bytes(2))
"""
#合包发送
g_sock.sendall((8190+8).to_bytes(4, byteorder="little") + (0).to_bytes(8004, byteorder="little"))
#分包
g_sock.sendall((0).to_bytes(190, byteorder="little"))


#一次发送
g_sock.sendall((100+8).to_bytes(4, byteorder="little"))
g_sock.sendall((0).to_bytes(104, byteorder="little"))







#合包发送
g_sock.sendall((100+8).to_bytes(4, byteorder="little"))
g_sock.sendall((0).to_bytes(104, byteorder="little") + (8190+8).to_bytes(4, byteorder="little") + (0).to_bytes(8004, byteorder="little"))
#分包
g_sock.sendall((1).to_bytes(190, byteorder="little"))


#一次发送
g_sock.sendall((100+8).to_bytes(4, byteorder="little"))
g_sock.sendall((0).to_bytes(104, byteorder="little"))

#最大长度的包
g_sock.sendall((8192+8).to_bytes(4, byteorder="little"))
g_sock.sendall((0).to_bytes(4, byteorder="little"))
g_sock.sendall((0).to_bytes(1000, byteorder="little"))
g_sock.sendall((0).to_bytes(7192, byteorder="little"))

"""
#超出最大长度的包
g_sock.sendall((8193+8).to_bytes(4, byteorder="little"))
g_sock.sendall((0).to_bytes(4, byteorder="little"))
g_sock.sendall((0).to_bytes(1000, byteorder="little"))
g_sock.sendall((0).to_bytes(7191, byteorder="little"))

#巨大的包
g_sock.sendall((100000+8).to_bytes(4, byteorder="little"))
g_sock.sendall((0).to_bytes(4, byteorder="little"))
g_sock.sendall(bytes(100000))
"""




g_sock.close()
#comm()
