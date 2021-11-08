def	text_analyzer(*ptr):
	'''Compte le nombre de lettre, minuscule, majuscule, espace ainsi que ponctuation'''
	import string
	if not ptr:
		text = []
		i = 0
		ptr = input("What is the text to analyse?\n")
	text = ptr
	print(text)
	maj = 0
	min = 0
	punctuation = 0
	space = 0
	lenght = 0
	lenght = sum([sum([c.isascii() for c in ptr2]) for ptr2 in text])
	maj = sum([sum([c.isupper() for c in ptr2]) for ptr2 in text]) 
	min = sum([sum([c.islower() for c in ptr2]) for ptr2 in text])
	punctuation = sum([sum([c in string.punctuation for c in ptr2]) for ptr2 in text])
	space = sum([sum([c in string.whitespace for c in ptr2]) for ptr2 in text])
	print("The text contains " + str(lenght) + ":")
	print("- " + str(maj) + " upper letters")
	print("- " + str(min) + " lower letters")
	print("- " + str(punctuation) + " punctuation marks")
	print("- " + str(space) + " spaces\n")
