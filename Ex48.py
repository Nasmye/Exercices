from string import *

class myString():
	
	"""docstring for myString"""
	def __init__(self ,liste):
		
		self.liste = liste

	def get_liste(self):
		return self.liste	

	def append(self, x):
		self.liste.append(x)
		

	def pop(self ,x):
		return self.liste.pop(x)


print(issubclass(myString,str))


l1= ['5',8,'c','d']	
l2 = myString(l1)

print(l2.get_liste())

l2.append('e')

print(l2.get_liste())

l1.pop(2)
print(l2.get_liste())


