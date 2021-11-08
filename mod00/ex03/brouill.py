def	text_analyzer(*ptr):
	import string
	if not ptr:
		ptr = input("What is the text to analyse?\n")
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
	print("The text contains " + str(lenght) + ":\n")
	print("- " + str(maj) + " upper letters\n")
	print("- " + str(min) + " lower letters\n")
	print("- " + str(punctuation) + " punctuation marks\n")
	print("- " + str(space) + " spaces\n\n")
	
text_analyzer("test")