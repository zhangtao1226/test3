import socket

server = socket.socket()
host = socket.gethostname()
port = 1234

server.connect((host, port))
print(server.recv(1024).decode("utf-8"))