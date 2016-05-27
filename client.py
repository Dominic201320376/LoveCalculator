import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(("10.150.243.219", 54321))

while True:
	data = clientsocket.recv(1024)
	print data
	clientsocket.send(raw_input())
