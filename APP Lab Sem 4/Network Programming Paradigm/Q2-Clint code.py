"""Write a ping-pong client and server application. When a client sends a ping message to the server, the server will respond with a pong message. Other messages sent by
the client can be safely dropped by the server"""
from socket import *
clnt_sock_331 = socket(AF_INET,SOCK_STREAM)
clnt_sock_331.connect(('localhost',9300))
msg_331 = clnt_sock_331.recv(1024)
print(msg_331)
print("Starting to talk.... \nEnter Your Message")
str_331 = input()
clnt_sock_331.send(str_331.encode())
msg1_331 = clnt_sock_331.recv(1024)
print(msg1_331)
clnt_sock_331.close()
