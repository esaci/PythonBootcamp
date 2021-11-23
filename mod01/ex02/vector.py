from typing import Union

import sys


class Vector:
	def	list_float(self, x):
		if isinstance(x, list) and all([isinstance(i, float) for i in x]):
			return 1
		return 0
	def list_list_float(self, x):
		if isinstance(x, list) and all([isinstance(j, list) and all([isinstance(i, float) for i in j]) for j in x]):
			if all(len(x[0]) == len(i) for i in x):
				return 1
		return 0
	def	adder(self, other):
		if not isinstance(other, Vector):
			print("Can only add two vectors", file=sys.stderr)
			exit()
		other : Vector
		if self.list_float(other.values) and self.list_float(self.values):
			if len(other.values) == len(self.values):
				return Vector([[float(i + j)] for (i,j) in zip(other.values,self.values)])
		if self.list_list_float(other.values) and self.list_list_float(other.values):
			if len(other.values) == len(self.values):
				if all([len(a) == len(b) for (a,b) in zip(other.values, self.values)]):
					return Vector([[float(x + y)] for (a,b) in zip(other.values, self.values) for (x,y) in zip(a,b)])
		print("Can only add two same shape vectors", file=sys.stderr)
		exit()
	def reducer(self, vect1, vect2):
		if not isinstance(vect2, Vector):
			print("Can only - between two vectors", file=sys.stderr)
			exit()
		vect2 : Vector
		if self.list_float(vect2.values) and self.list_float(vect1.values):
			if len(vect2.values) == len(vect1.values):
				return Vector([[float(i - j)] for (i,j) in zip(vect2.values,vect1.values)])
		if self.list_list_float(vect2.values) and self.list_list_float(vect2.values):
			if len(vect2.values) == len(vect1.values):
				if all([len(a) == len(b) for (a,b) in zip(vect2.values, vect1.values)]):
					return Vector([[float(x - y)] for (a,b) in zip(vect2.values, vect1.values) for (x,y) in zip(a,b)])
		print("Can only - two same shape vectors", file=sys.stderr)
		exit()
	def diviser(self, vect1, vect2):
		if not isinstance(vect2, Vector):
			print("Can only - between two vectors", file=sys.stderr)
			exit()
		vect2 : Vector
		if self.list_float(vect2.values) and self.list_float(vect1.values):
			if len(vect2.values) == len(vect1.values):
				if all([j != 0] for j in vect2.values):
					return Vector([[float(i / j)] for (i,j) in zip(vect2.values,vect1.values)])
		if self.list_list_float(vect2.values) and self.list_list_float(vect2.values):
			if len(vect2.values) == len(vect1.values):
				if all([len(a) == len(b) for (a,b) in zip(vect2.values, vect1.values)]):
					return Vector([[float(x / y)] for (a,b) in zip(vect2.values, vect1.values) for (x,y) in zip(a,b)])
		print("Can only - two same shape vectors", file=sys.stderr)
		exit()
	def __init__(self, x ):
		if not x:
			print("class value need one argument")
		if self.list_float(x):
			self.values = x
		elif self.list_list_float(x):
			self.values = x
		elif isinstance(x, float) or isinstance(x, int):
			self.values = [[float(i), float(0)] for i in range(0, int(x))]
		else:
			print("Error, argument n'est ni une list de float, ni une liste de liste de float", file=sys.stderr)
			exit()
	def	shape(self):
		if self.list_list_float(self.values):
			return (sum([1 for i in self.values]), sum([1 for i in self.values[0]]))
		if self.list_float(self.values):
			return (1, sum([1 for i in self.values]))
		print("error, not a vector", file=sys.stderr)
	def __add__(self, other):
		return self.adder(other)
	def __radd__(self, other):
		return self.adder(other)
	def __sub__(self, other):
		self.reducer(self, other)
	def __rsub__(self, other):
		self.reducer(other, self)
	def __truediv__(self, other):
	def __rtruediv__(self, other):

