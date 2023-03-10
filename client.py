import socket

s = socket.socket(socket.AF_INEt, socket.SOCK_STREAM)
s.connect(('77.88.8.8', 80))

connection = socket.socket(socket.AF_INEt, socket.SOCK_STREAM)
IP=str(s.getsockname()[0])

PORT=12333
connection.connect((IP, PORT))
rd=connection.recv(1024)
print(rd.decode('utf8'))
connection.send("Hello and you!".encode('utf8'))
connection.close()
