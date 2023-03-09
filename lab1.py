import socket
import http.client
import uuid, re

print("PC Name: " + socket.gethostname())
conn=http.client.HTTPConnection("ifconfig.me")
conn.request("GET","/ip")
print("IP: " + str(conn.getresponse().read()))

#print("IP: " + socket.gethostbyname(socket.gethostname()))

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 80))
print("IP: " + s.getsockname()[0])
print(":".join(re.findall('..', '%012x' % uuid.getnode())))
