import sys

if (len(sys.argv) < 2):
	exit()
for ptr in sys.argv[1:]:
	for c in ptr:
		if not c.isalnum() and c != ' ':
			print("ERROR")
			exit()
morse = {
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
    }
res = ""
for tmp in sys.argv[1:]:
	if not tmp == sys.argv[1]:
		res += "/ "
	ptr = tmp.lower()
	for c in ptr:
		if c != ' ':
			res += morse[c]
		else:
			res += "/"
		res += " "
print(res)