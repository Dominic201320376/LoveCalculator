class FlamesCalculator:
	
	def __init__(self, name1, name2):
		self.name1 = name1
		self.name2 = name2
		self.flamesCount = 0
		self.result = "FLAMES"

		self.calculateCount()
		self.calculateResult()

	def remove(self, stringToBeAltered, delimiter, count):
		string = stringToBeAltered.split(delimiter, count)
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
		return self.result