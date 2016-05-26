from re import sub
from FlamesCalculator import FlamesCalculator
from TrueLoveCalculator import TrueLoveCalculator
from InputValidator import InputValidator
import socket
from threading import Thread

def client(connection):
	connection.send("Choose algorithm\n1:FLAMES\n2:TRUE LOVE\n")
	choice = connection.recv(1024)
	while True:
		connection.send("Names: ")
		names = connection.recv(1024)
		verifier = InputValidator()

		if(verifier.validate(names)):
			names = sub(r'\s+', '', names)
			name1,name2 = names.lower().split(",")

			if(choice == "1"):
				flame = FlamesCalculator(name1, name2)
				connection.send(flame.output() + "\nPress enter to continue")

			elif(choice == "2"):
				trueLove = TrueLoveCalculator(name1, name2)
				connection.send(trueLove.output() + "\nPress enter to continue")
			else:
				connection.send("Invalid Input" + "\nPress enter to continue")
		else:
			connection.send("Invalid Input" + "\nPress enter to continue")
		# add timer

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('', 54321))
serversocket.listen(5)

while True:
	connection, address = serversocket.accept()
	
	thread = Thread(target = client, args = (connection, ))
	thread.start()
	print "Starting new thread"

thread.join()