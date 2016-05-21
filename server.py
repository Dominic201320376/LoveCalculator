from re import sub

class InputVerification:
	def validate(self, string):
		if "," not in string:
			return False
		return True

class Flames:
	def __init__(self, name1, name2):
		self.name1 = name1
		self.name2 = name2
		self.flamesCount = 0
		self.result = "FLAMES"

		self.calculateCount()
		self.calculateResult()
		self.output()

	def remove(self, stringToBeAltered, delimeter, count):
		string = stringToBeAltered.split(delimeter, count)
		return string[0] + string[1]

	def calculateCount(self):
		for char in self.name1:
			if char in self.name2:
				self.name1 = self.remove(self.name1, char, 1)
				self.name2 = self.remove(self.name2, char, 1)

		self.flamesCount = len(self.name1+self.name2)

	def calculateResult(self):
		charCount = 0

		while len(self.result) > 1:
			charCount += (self.flamesCount % len(self.result)) - 1
			charCount %= len(self.result)

			self.result = self.remove(self.result, self.result[charCount], 1)

	def output(self):
		print self.result

class TrueLove:
	def __init__(self, name1, name2):
		self.name1 = name1
		self.name2 = name2
		self.trueLove = {"t" : 0, "r" : 0, "u" : 0, "e" : 0, "l" : 0, "o" : 0, "v" : 0}

		self.count(self.name1)
		self.count(self.name2)

		self.result()

	def count(self, string):
		for char in string:
			if char in self.trueLove:
				self.trueLove[char] += 1

	def result(self):
		true = self.trueLove["t"] + self.trueLove["r"] + self.trueLove["u"] + self.trueLove["e"]
		love = self.trueLove["l"] + self.trueLove["o"] + self.trueLove["v"] + self.trueLove["e"]

		print true*10 + love


names = raw_input("Names ")

verifier = InputVerification()

if(verifier.validate(names)):
	names = sub(r'\s+', '', names)
	name1,name2 = names.lower().split(",")

	choice = raw_input("Choose algorithm\n1:FLAMES\n2:TRUE LOVE\n")

	if(choice == "1"):
		Flames(name1, name2)
	elif(choice == "2"):
		TrueLove(name1, name2)
	else:
		print "Invalid Input"
else:
	print "Invalid Input"