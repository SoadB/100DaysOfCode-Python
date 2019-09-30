

class MyClass:
	x = 5


print(MyClass)
print("-------------------------")

p1 = MyClass()
print(p1.x)


class Person:
	def __init__(self, name , age):
		self.name = name
		self.age = age

	def myfun(abc):
		print("Hello my name is "+ abc.name)


p1 = Person("Soad", 25)
print(p1.name, p1.age)
p1.myfun()
print("-------------------------")



