import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('77.88.8.8', 80))
print(s.getsockname()[0])
#listener=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#IP = str(s.getsockname()[0])
#PORT=12333
#listener.bind((IP, PORT))

#listener.listen(0)

#connection, address=listener.accept()

#connection.send("Hello, connect!".encode('utf8'))

#connection.send("Hello!".encode('utf8'))

#while True:
#	data_output=''
#	while True:
#		data=connection.recv(1024).decode('utf8')
#		data_output+=data
#		if not data:
#			break
#	print(data_output)
