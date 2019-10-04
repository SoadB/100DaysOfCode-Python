

class Person:
	def __init__(self, fname, lname):
		self.firstname = fname
		self.lastname = lname

	def printname(self):
		print(self.firstname, self.lastname)


class Student(Person):
	def __init__(self, fname, lname, year):
		super().__init__(fname, lname)
		self.graduationyear = year

	def welcom(self):
		print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


x = Student('Mike', 'Olsen', 2019)
x.printname()
print("-------------------------")

print(x.graduationyear)
print("-------------------------")

x.welcom()

