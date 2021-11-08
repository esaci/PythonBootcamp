def	text_analyzer(*ptr3):
	import string
	ptr[][]
	if not ptr3:
		ptr2 = input("What is the text to analysee?\n")
		ptr += ptr2
		print("je passe ici au moins")
		while 1:
			ptr2 = input("What is the text to analyse?\n")
			ptr += ptr2
	else
		ptr = ptr3
	maj = 0
	min = 0
	punctuation = 0
	space = 0
	lenght = 0
	lenght = sum([sum([c.isascii() for c in ptr2]) for ptr2 in ptr])
	maj = sum([sum([c.isupper() for c in ptr2]) for ptr2 in ptr]) 
	min = sum([sum([c.islower() for c in ptr2]) for ptr2 in ptr])
	punctuation = sum([sum([c in string.punctuation for c in ptr2]) for ptr2 in ptr])
	space = sum([sum([c in string.whitespace for c in ptr2]) for ptr2 in ptr])
	print("The text contains " + str(lenght) + ":")
	print("- " + str(maj) + " upper letters")
	print("- " + str(min) + " lower letters")
	print("- " + str(punctuation) + " punctuation marks")
	print("- " + str(space) + " spaces\n")
	