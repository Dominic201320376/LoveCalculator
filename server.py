from re import sub
from FlamesCalculator import FlamesCalculator
from TrueLoveCalculator import TrueLoveCalculator
from InputVerification import InputVerification

names = raw_input("Names ")

verifier = InputVerification()

if(verifier.validate(names)):
	names = sub(r'\s+', '', names)
	name1,name2 = names.lower().split(",")

	choice = raw_input("Choose algorithm\n1:FLAMES\n2:TRUE LOVE\n")

	if(choice == "1"):
		flame = FlamesCalculator(name1, name2)
		print flame.output()

	elif(choice == "2"):
		trueLove = TrueLoveCalculator(name1, name2)
		print trueLove.output()
	else:
		print "Invalid Input"
else:
	print "Invalid Input"