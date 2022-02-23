""" Write a Socket-based Python server program that responds to client messages as follows: When it receives a message from a client, it simply converts the message into all 
uppercase letters and sends back the same to the client. Write both client and server programs demonstrating this. """
from socket import *
srvr_sock_331 = socket(AF_INET,SOCK_STREAM)
srvr_sock_331.bind(('localhost',9300))
srvr_sock_331.listen(5)
print("Server started....")
while True:
    tpl_331 = srvr_sock_331.accept()
    wel_msg_331 = "Welcome client %s"%tpl_331[1][0]
    conn_331 = tpl_331[0]
    conn_331.send(wel_msg_331.encode())
    rec_msg_331=conn_331.recv(1024)
    str_331=rec_msg_331.decode()
    s_331=str_331.upper()
    wel_msg1_331 = "Message in Uppercase is : %s"%s_331
    conn_331 = tpl_331[0]
    conn_331.send(wel_msg1_331.encode())
