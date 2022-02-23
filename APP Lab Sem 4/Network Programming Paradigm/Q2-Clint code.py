""" Write a Socket-based Python server program that responds to client messages as follows: When it receives a message from a client, it simply converts the message into all 
uppercase letters and sends back the same to the client. Write both client and server programs demonstrating this. """
from socket import *
clnt_sock_331 = socket(AF_INET,SOCK_STREAM)
clnt_sock_331.connect(('localhost',9300))
msg_331 = clnt_sock_331.recv(1024)
print(msg_331)
print(type(msg_331))
print("Starting to talk.... \nEnter Your Message")
str_331 = input()
clnt_sock_331.send(str_331.encode())
msg1_331 = clnt_sock_331.recv(1024)
print(msg1_331)
clnt_sock_331.close()
