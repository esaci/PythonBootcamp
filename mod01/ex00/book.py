import datetime as dt
from datetime import datetime
from typing import List
import recipe as rp

class Book:
	def __init__(self, *ptr):
		count = 0
		if not ptr or len(ptr) != 4:
			print("Error, Book necessite 4 arguments: name, last_update, creation_date, recipes_list")
		elif not ptr[0] or type(ptr[0]) != str:
			print("Error, name must be a non-empty string")
		elif not ptr[1] or type(ptr[1]) != dt.datetime:
			print("Error, last_update must be a datetime variable")
		elif not ptr[2] or type(ptr[2]) != dt.datetime:
			print("Error, creation_date must be a datetime variable")
		elif not ptr[3] or type(ptr[3]) != dict:
			print("Error, recipes_list must be a dictionnary")
		elif len(ptr[3]) != 3:
			print("recipe_list must contain starter, lunch, dessert")
		elif sum([i not in ["starter", "lunch", "dessert"] for i in ptr[3]]):
			print("recipe_list must only contain starter, lunch, dessert")
		elif sum([type(ptr[3][i]) != list for i in ptr[3]]):
			print("Il y a un element dans le dict recipes_list qui n'est pas une list")
		elif sum([type(j) != rp.recipe for i in ptr[3] for j in ptr[3][i]]):
			print("Il y a un element dans l'une des listes du dict recipes_list qui n'est pas une recette")
		else:
			count += 1
		if	count == 0:
			exit()
		count = 0
		self.name = ptr[count]
		count += 1
		self.last_update = ptr[count]
		count += 1
		self.creation_date = ptr[count]
		count += 1
		self.recipes_list = ptr[count]
		for i in self.recipes_list:
			i : list
	def get_recipe_by_name(self, name):
		if not name or type(name) != str:
			print("Error, get_recipe_by_name argument must be a string")
			exit()
		for i in self.recipes_list:
			for j in self.recipes_list[i]:
				if j.name == name:
					print(str(j))
					return j
		print("Error, No recipe with this name")
		exit()
	def get_recipe_by_type(self, recipe_type):
		if (not recipe_type or recipe_type not in ["starter", "lunch", "dessert"]):
			print("Error, get_recipe_by_type first argument must be in [starter, lunch, dessert]")
			exit()
		for i in self.recipes_list:
			if sum([1 for j in self.recipes_list[i] if i == recipe_type]):
				return [j for j in self.recipes_list[i] if i == recipe_type]
	def add_recipe(self, recipe):
		if not recipe or type(recipe) != rp.recipe:
			print("Error, add_recipe need a recipe as argument")
			exit()
		temp = rp.recipe(recipe.name, recipe.cooking_lvl,\
			recipe.cooking_time, recipe.ingredients, recipe.description, recipe.recipe_type)
		tempi = self.recipes_list[recipe.recipe_type]
		tempi.append(temp)
		now = datetime.now()
		self.last_update = now

		




					