
class recipe:
	def check0(self, ptr2):
		if not ptr2:
			print("Error, name{:s} empty".format(str(ptr2)))
		elif type(ptr2) != str:
			print("Error, name {:s} wrong type".format(str(ptr2)))
		else:
			return True
		return False
	def	check1(self, ptr2):
		if (type(ptr2) != int):
			print("Error, cooking_lvl {:s} not int".format(str(ptr2)))
		elif ptr2 not in [i for i in range(1, 6)]:
			print("Error, cooking_lvl {:s} not in [1, 5]".format(str(ptr2)))
		else:
			return True
		return False
	def check2(self, ptr2):
		if type(ptr2) != int:
			print("Error, cooking_time {:s} not int".format(str(ptr2)))
		elif ptr2 < 0:
			print("Error, cooking_time {:s} negativ".format(str(ptr2)))
		else:
			return True
		return False
	def	check3(self, ptr2):
		if not ptr2:
			print("Error, ingredients empty")
		if type(ptr2) != list:
			print("Error, ingredients not a list")
		elif sum(type(ptr) != str for ptr in ptr2):
			print("Error, In ingredients an element isn't a string{:}".format(ptr2))
		else:
			return True
		return False
	def	check5(self, ptr2):
		if (type(ptr2) != str):
			print("Error, recipe_type not string")
		elif ptr2 not in ["starter", "lunch", "dessert"]:
			print("Error, recipe_type not in {:}".format(["starter", "lunch", "dessert"]))
		else:
			return True
		return False
	def	checker(self, ptr2, count):
		if (count == 0):
			return self.check0(ptr2)
		if (count == 1):
			return self.check1(ptr2)
		if (count == 2):
			return self.check2(ptr2)
		if count == 3:
			return self.check3(ptr2)
		if (count == 4 and type(ptr2) != str):
			print("Error, Description wrong type")
			return False
		if (count == 5):
			return self.check5(ptr2)
		return True
	def __init__(self, *ptr):
		if not ptr or len(ptr) != 6:
			if len(ptr) > 6 :
				print("Error, Trop d'argument")
			else :
				print("Error, Pas assez d'argument")
			exit()
		count = 0
		for ptr2 in ptr:
			if not self.checker(ptr2, count):
				exit()
			count += 1
		count = 0
		self.name = ptr[count]
		count += 1
		self.cooking_lvl = ptr[count]
		count += 1
		self.cooking_time = ptr[count]
		count += 1
		self.ingredients = ptr[count]
		count += 1
		self.description = ptr[count]
		count += 1
		self.recipe_type = ptr[count]
	def __str__(self):
		txt = ""
		txt += "Nom de la recette: " + self.name + "\n" + "Recette de niveau: " + str(self.cooking_lvl)
		txt += "\nDuree de la preparation: " + str(self.cooking_time) + "\nIngredients: " + str(self.ingredients)
		txt += "\nPeut etre mange au: " + self.recipe_type
		return txt