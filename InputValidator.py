class InputValidator:
	
	def validate(self, string):
		if "," not in string:
			return False
		# check count of , if not equal to 1 return False
		# check for at least one character before and after , if none return False
		return True