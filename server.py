from re import sub

class InputVerification:
	def validate(self, string):
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
		#removes whitespaces
		self.name1 = sub(r'\s+', '', self.name1)
		self.name2 = sub(r'\s+', '', self.name2)

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

name1 = raw_input("First Name ")
name2 = raw_input("Second Name ")

verifier = InputVerification()

if(verifier.validate(name1) and verifier.validate(name2)):
	Flames(name1, name2)