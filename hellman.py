import socket 
import random

p=7237
g=26

a=random.randint(1,p-2)
A=pow(g,a,p)
print(f"[Server] p={p}, g={g}, private a={a}, public A={A}")

server_socket=socket.socket()
server_socket.bind(('localhost',5000))

server_socket.listen(1)
conn,addr=server_socket.accept()


conn.send(str(A).encode())


B=int(conn.recv(1024).decode())
print(f"[Server] Received B={B}")

shared_secret=pow(B,a,p)
print(f"[Server] Shared secret = {shared_secret}")
conn.close()
server_socket.close()