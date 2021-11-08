import sys

ptr = ""

for ptr2 in sys.argv[:0:-1]:
	if ptr2 != sys.argv[-1]:
		ptr += " "
	ptr += ptr2[::-1].swapcase()
print(ptr)