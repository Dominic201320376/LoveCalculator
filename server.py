#Program only tested on Linux with Python 2.7

from re import sub
import sys, select
from FlamesCalculator import FlamesCalculator
from TrueLoveCalculator import TrueLoveCalculator
from InputValidator import InputValidator
import socket
from threading import Thread

def client(connection):
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

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('', 54321))
serversocket.listen(5)

while True:

	print("Choose algorithm\n1:FLAMES\n2:TRUE LOVE\n")
	print("You have ten seconds to answer")
	str1, temp1, temp2 = select.select( [sys.stdin], [], [], 10 )

	if(str1):
		choice = sys.stdin.readline().strip()
	else:
		choice = "1"
		print "Choice defaulted to FLAMES\n"

	if choice == "1" or choice == "2":
		break
		
	print "Invalid Input"


while True:
	connection, address = serversocket.accept()
	
	thread = Thread(target = client, args = (connection, ))
	thread.start()
	print "Starting new thread"

thread.join()