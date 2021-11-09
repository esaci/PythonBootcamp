import time
import sys

def ft_progress(lst):
	count = 0
	for ptr in lst:
		count += 1
		sys.stdout.write("ETA: {:d} [{:3d}]   \r" % ((100 * count)/len(lst)) )
		sys.stdout.flush()
		yield ptr

listy = range(1000)

ret = 0
for elem in ft_progress(listy):
	ret += (elem + 3) % 5
	time.sleep(0.01)
print()
print(ret)