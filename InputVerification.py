class InputVerification:
	
	def validate(self, string):
		if "," not in string:
			return False
		return True