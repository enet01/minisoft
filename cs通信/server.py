#!-*- coding:utf-8 -*-
import socket
from time import sleep
HOST="0.0.0.0"
PORT=8080
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(2)
while True:
	conn,addr=s.accept()
	print "connect to by,",addr
	while True:
		data=conn.recv(2048)
		print data
		if not data:
			sleep(1)
			continue
		conn.sendall(data)
conn.close()
	
