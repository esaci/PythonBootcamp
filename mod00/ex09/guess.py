import random

def boucle(tentatives):
	ptr = input("What is your guess between 1 and 99: ")
	tentatives[0] += 1
	if ptr == "exit":
		exit()
	if not ptr.isnumeric():
		print("That's not a number")
		return (boucle(tentatives))
	return (ptr)


val = random.randint(1, 99)
tentatives = []
tentatives.append(0)
print("You have to guess a number between 1 and 99 to find out the secret number")
print("Type 'exit' to end the game")
dev = val - 1
while (int(dev) != val):
	dev = boucle(tentatives)
	if (int(dev) > val):
		print("Too high!")
	if (int(dev) < val):
		print("Too low!")
if (val == 42):
	print("The answer to the ultimate question of life, the universe and everything is 42")
if (tentatives[0] == 1):
	print("Congratulations, You got it a your FIRST try")
else:
	print("Congratulations, you got it on your {:d} attempt".format(tentatives[0]))