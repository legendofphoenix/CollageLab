"""Write a ping-pong client and server application. When a client sends a ping message to the server, the server will respond with a pong message. Other messages sent by the 
client can be safely dropped by the server"""
from socket import *
srvr_sock_331 = socket(AF_INET,SOCK_STREAM)
srvr_sock_331.bind(('localhost',9300))
srvr_sock_331.listen(5)
print("Server started....")
while True:
tpl_331 = srvr_sock_331.accept()
wel_msg_331 = "Welcome client!"
conn_331 = tpl_331[0]
conn_331.send(wel_msg_331.encode())
rec_msg_331=conn_331.recv(1024)
str_331=rec_msg_331.decode()
if(str_331 == 'ping'):
wel_msg1_331="pong"
conn_331 = tpl_331[0]
conn_331.send(wel_msg1_331.encode())
