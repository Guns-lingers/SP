import socket

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('77.88.8.8', 80))

listener=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
IP = str(s.getsockname()[0])
PORT=12333

listener.bind((IP, PORT))
data, address=listener.recvfrom(1024)
listener.sendto(data, address)
