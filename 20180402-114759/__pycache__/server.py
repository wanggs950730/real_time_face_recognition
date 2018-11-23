#coding=utf-8
#!/usr/bin/env python 

from socket import socket,AF_INET,SOCK_STREAM
import threading
import time

HOST=''
PORT=2159
BUFSIZ=1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
socks=[] #放每个客户端的socket

def handle():
    while True:
        for s in socks:
            try:
                data = s.recv(BUFSIZ) #到这里程序继续向下执行
            except Exception:
                continue
            if not data:
                socks.remove(s)
                continue
            s.send('[%s],%s' % (ctime(), data))

t = threading.Thread(target=handle) #子线程

if __name__ == '__main__':
    t.start()

    while True:
        clientSock,addr = tcpSerSock.accept()
        clientSock.setblocking(0)
        socks.append(clientSock)
        