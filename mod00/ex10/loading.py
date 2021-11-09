import time
import sys

def ft_progress(lst):
	count = 0
	for ptr in lst:
		count += 1
		ptr4 = ""
		for i in range (0, int((10 * count)/len(lst))):
			ptr4 += "="
		for i in range(int((10 * count)/len(lst)), 11):
			ptr4 += " "
		sys.stdout.write("ETA: [{:03d}] [{:}>]  \r".format(int((100 * count)/len(lst)), ptr4))
		sys.stdout.flush()
		yield ptr

listy = range(1000)

ret = 0
for elem in ft_progress(listy):
	ret += (elem + 3) % 5
	time.sleep(0.01)
print()
print(ret)