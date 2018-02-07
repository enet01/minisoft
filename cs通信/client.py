#!-*- coding:utf-8 -*-
import socket
HOST="192.168.5.63"
PORT=8080

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
while True:
        string=raw_input(">")
        if string=="quit":break
        s.sendall(string)
        data=s.recv(2048)
        print "received",str(data)

s.close()
