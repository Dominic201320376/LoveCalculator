class TrueLoveCalculator:

	def __init__(self, name1, name2):
		self.name1 = name1
		self.name2 = name2
		self.trueLove = {"t" : 0, "r" : 0, "u" : 0, "e" : 0, "l" : 0, "o" : 0, "v" : 0}

		self.count(self.name1)
		self.count(self.name2)

		self.output()

	def count(self, string):
		for char in string:
			if char in self.trueLove:
				self.trueLove[char] += 1

	def output(self):
		true = self.trueLove["t"] + self.trueLove["r"] + self.trueLove["u"] + self.trueLove["e"]
		love = self.trueLove["l"] + self.trueLove["o"] + self.trueLove["v"] + self.trueLove["e"]

		return true*10 + love