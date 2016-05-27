from re import sub
class InputValidator:
	
	def validate(self, string):
		if string.count(",")!=1:
			return False
		else:
			str1,str2 = sub(r'\s+', '', string).split(",")
			if len(str1) < 1 or len(str2) < 1 or str1.isalpha() == False or str2.isalpha() == False:
				return False
		return True