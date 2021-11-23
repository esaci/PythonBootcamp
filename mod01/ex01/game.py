class GotCharacter:
	'''A class reprensenting a got char'''
	def __init__(self, first_name, is_alive=True):
		if not first_name or type(first_name) != str:
			print("first_name doit etre une str")
		self.first_name = first_name
		self.is_alive = is_alive
class Stark(GotCharacter):
	'''A class representing a Stark member'''
	def __init__(self, family_name = "Stark", house_words = "Winter is coming"):
		self.family_name = family_name
		self.house_words = house_words
	def print_house_words(self):
		print(self.house_words)
	def	die(self):
		self.is_alive = False