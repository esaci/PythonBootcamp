dicosand = {'ingredients' : ["ham", "bread", "cheese", "tomatoes"], 'meal' : "lunch", 'prep_time' : 10 }
cookbook = {'sandwich' : dicosand}
cookbook['cake'] = {'ingredients' : ["floor", "sugar", "eggs"], 'meal' : "dessert", 'prep_time' : 60 }
cookbook['salad'] = {'ingredients' : ["avocado", "arugula", "tomatoes", "spinach"], 'meal' : "lunch", 'prep_time' : 15}

def	print_recipe(ptr=""):
	if not ptr:
		print("Necessite une recette en argument")
		return
	for rr in cookbook:
		if rr == ptr:
			print("Recipe for {:s}:\nIngredients list: {:}\nTo be eaten for {:s}\nTakes {:d} minutes of cooking.\
				".format(ptr, (cookbook[ptr]['ingredients']), cookbook[ptr]['meal'], cookbook[ptr]['prep_time']))
			return
	print("Pas de recette associe")

def	del_recipe(ptr=""):
	if not ptr:
		print("Necessite une recette en argument")
		return
	for rr in cookbook:
		if rr == ptr:
			del(cookbook[ptr])
			return
	print("Pas de recette associe")

def add_recipe(name, ptr, mealtype, prepo):
	if not name or not ptr or not mealtype or not prepo or not prepo.isnumeric():
		print("Necessite 4 arguments: Nom recette, Ingredients, Meal type, Preparation time")
		return
	cookbook[name] = {'ingredients': ptr, 'meal' : mealtype, 'prep_time' : int(prepo)}

def	print_all_recip():
	for j in cookbook:
		print_recipe(j)
		print("")
	return

def boucle():
	ptr = input("Please select an option by typing the corresponding number:\n1: Add a recipe\
		\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit\n")
	while not ptr.isnumeric():
		print("This option does not exist, please type the corresponding number.")
		ptr = input("Please select an option by typing the corresponding number:\n1: Add a recipe\n\
		2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit")
	return (ptr)

ptr = boucle()
while (int(ptr) != 5):
	if int(ptr) == 1:
		ptr2 = []
		ptr2.append(input("Please enter Nom recette: "))
		ptr2.append(input("Please enter  Ingredients: ").split())
		ptr2.append(input("Please enter Meal type: "))
		ptr2.append(input("Please enter prep_time: "))
		add_recipe(ptr2[0], ptr2[1], ptr2[2], ptr2[3])
	elif int(ptr) == 2:
		ptr2 = input("Please enter : Nom recette to delete: ")
		del_recipe(ptr2)
	elif int(ptr) == 3:
		ptr2 = input("Please enter : Nom recette to print: ")
		print_recipe(ptr2)
	elif int(ptr) == 4:
		print_all_recip()
	else:
		print("This option does not exist")
	ptr = boucle()
print("Cookbook closed.")