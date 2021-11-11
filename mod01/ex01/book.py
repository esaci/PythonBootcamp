import datetime as dt

class Book:
	def __init__(self, *ptr):
		if not ptr or len(ptr) != 4:
			print("Error, Book necessite 4 arguments: name, last_update, creation_date, recipes_list")
			exit()
		if not ptr[0] or type(ptr[0]) != str:
			print("Error, name must be a non-empty string")
			exit()
		if not ptr[1] or type(ptr[1]) != dt.datetime:
			print("Error, last_update must be a datetime variable")
			exit()
		if not ptr[2] or type(ptr[2]) != dt.datetime:
			print("Error, creation_date must be a datetime variable")
			exit()
		if not ptr[3] or type(ptr[3]) != dict:
			print("Error, recipes_list must be a dictionnary")
			exit()
		if len(ptr[3]) != 3:
			print("recipe_list must contain starter, lunch, dessert")
		if sum([i not in ["starter", "lunch", "dessert"] for i in ptr[3]]):
			print("recipe_list must only contain starter, lunch, dessert")