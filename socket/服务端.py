import socket

server = socket.socket()
host = socket.gethostname()
port = 1234
server.bind((host,port))
server.listen(5)

while True:
    c, addr = server.accept()
    print('Got connection from', addr)
    c.send('打印中文'.encode("utf-8"))
    c.close()