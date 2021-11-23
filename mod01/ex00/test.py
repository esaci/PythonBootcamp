import book as bk
import recipe as rp
import datetime as dt

lol4 = rp.recipe("elias", 5, 10, ["choco", "croc"], "delicieux", "lunch")
lol = rp.recipe("test", 5, 10, ["gateau", "sucre"], "delicieux", "lunch")
""" print(str(lol)) """
lol2 = rp.recipe("test2", 5, 10, ["gateau", "sucre"], "delicieux", "dessert")
lol3 = rp.recipe("test3", 5, 10, ["gateau", "sucre"], "delicieux", "starter")
old = dt.datetime(2021,4, 1, 14, 30, 22, 2)
test = bk.Book("elias", old, old, {"starter" : [lol3], "lunch" : [lol], "dessert" : [lol2]})
for i in test.get_recipe_by_type("lunch"):
	print(str(i))
test.add_recipe(lol4)
print ("-------------------------------------")
for i in test.get_recipe_by_type("lunch"):
	print(str(i))