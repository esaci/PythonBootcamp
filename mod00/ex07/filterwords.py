import sys
import string

if (len(sys.argv) != 3):
	print("Need two arguments")
	exit()
if (not sys.argv[0] or not sys.argv[2].isnumeric()):
	print("First Argumet must be a string, second a int")
	exit()
ptr3 = ""
for c in sys.argv[1]:
	if not c in string.punctuation:
		ptr3 += c
ptr2 = ptr3.split()
res = []
for ptr in ptr2:
	if (len(ptr) > int(sys.argv[2])):
		res.append(ptr)
print(res)
