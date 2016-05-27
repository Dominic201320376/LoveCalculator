class InputValidator:
	
	def validate(self, string):
		if string.count(",")!=1:
			return False
		else:
			str1,str2 = string.split(",")
			if len(str1) < 1 or len(str2) < 1 or str1.isalpha() == False or str2.isalpha() == False:
				return False
		# check count of , if not equal to 1 return False
		# check for at least one character before and after , if none return False
		return True