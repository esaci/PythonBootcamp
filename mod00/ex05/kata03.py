phrase = "The right format"

i = 0
for c in phrase:
	i += 1
ptr = ""
for d in range (i, 41):
	ptr += "-"
ptr += phrase
print(ptr)