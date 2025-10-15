import socket
import random

p=7237
g=26

b = random.randint(1, p-2)
B = pow(g, b, p)
print(f"[Client] p={p}, g={g}, private b={b}, public B={B}")

client_socket = socket.socket()
client_socket.connect(('localhost', 5000))

A = int(client_socket.recv(1024).decode())
print(f"[Client] Received A={A}")

client_socket.send(str(B).encode())

shared_secret = pow(A, b, p)
print(f"[Client] Shared secret = {shared_secret}")

client_socket.close()
