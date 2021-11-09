import sys
import numpy as np

if (len(sys.argv) != 3):
	print("need two number")
	exit()
if not sys.argv[1].isnumeric() or not sys.argv[2].isnumeric():
	print("need two number")
	exit()
print("Sum:              ", sum([int(ptr) for ptr in sys.argv[1:]]))
print("Difference:       ", int(sys.argv[1]) - sum([int(ptr) for ptr in sys.argv[2:]]))
print("Product:          ", np.prod([int(ptr) for ptr in sys.argv[1:]]))
if int(sys.argv[2]):
	print("Quotient:     ", int(sys.argv[1]) / int(sys.argv[2]))
else:
	print("Quotient:          ERROR (div by zero)")
if int(sys.argv[2]):
	print("Remainder:        ", int(sys.argv[1]) % int(sys.argv[2]))
else:
	print("Remainder:         ERROR (modulo by zero)")