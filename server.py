import socket

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('77.88.8.8', 80))

listener=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
IP = str(s.getsockname()[0])
PORT=12333
listener.bind((IP, PORT))

listener.listen(0)

connection, address=listener.accept()

connection.send("Hello, connect!\n".encode('utf8'))

connection.send("Hello!\n".encode('utf8'))

while True:
	data_output=''
	while True:
		data=connection.recv(1024).decode('utf8')
		data_output+=data
		if not data:
			break
	print(data_output)
