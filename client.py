import socket
import threading

def read_sok():
	while 1:
		data=sor.recv(1024)
		print(data.decode('utf8'))

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('77.88.8.8', 80))
PORT=12333
server = str(s.getsockname()[0]), PORT
alias=input("input your nickname: ")
sor=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sor.bind(('',0))
sor.sendto((alias+' Connect to server').encode('utf8'), server)
potok=threading.Thread(target=read_sok)
potok.start()
while 1:
	mensahe = input()
	sor.sendto(('['+alias+']'+mensahe).encode('utf8'), server)
