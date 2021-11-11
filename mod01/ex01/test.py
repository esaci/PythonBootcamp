import book as bk
import recipe as rp
import datetime as dt

lol = rp.recipe("test", 5, 10, ["gateau", "sucre"], "delicieux", "lunch")
print(str(lol))
old = dt.datetime(2021,4, 1, 14, 30, 22, 2)
test = bk.Book("elias", old, old, {"starter" : "delice", "lunch" : "midi", "dessert" : "koko"})
""" lol = rp.recipe(1, 5, 10, ["gateau", "sucre"], "delicieux", "lunch")
lol = rp.recipe("test", 6, 10, ["gateau", "sucre"], "delicieux", "lunch")
lol = rp.recipe("test", 5, "lol", ["gateau", "sucre"], "delicieux", "lunch")
lol = rp.recipe("test", 5, 10, [1, "sucre"], "delicieux", "lunch")
lol = rp.recipe("test", 5, 10, ["gateau", "sucre"], 2, "lunch")
lol = rp.recipe("test", 5, 10, ["gateau", "sucre"], "delicieux", 3)
lol = rp.recipe("", 5, 10, ["gateau", "sucre"], "delicieux", "lunch")
lol = rp.recipe("elias", -1, 10, ["gateau", "sucre"], "delicieux", "lunch") """