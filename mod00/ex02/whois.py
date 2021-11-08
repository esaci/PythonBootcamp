import sys

if len(sys.argv) != 2 or not sys.argv[1].isnumeric():
	print("ERROR")
	exit()
i = int(sys.argv[1])
if not i:
	print("I'm Zero")
	exit()
if not i % 2:
	print("I\'m Even")
	exit()
print("I'm O	dd")