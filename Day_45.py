
mytuple = ('apple', 'banana', 'cherry')
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
print("-------------------------")

mystr = 'Python'
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print("-------------------------")

mytuple = ('apple', 'banana', 'cherry')

for x in mytuple:
	print(x)
print("-------------------------")

mystr = 'Python'
for x in mystr:
	print(x)
print("-------------------------")

class MyNumbers:
	def __iter__(self):
		self.a = 1
		return self

	def __next__(self):
		x = self.a
		self.a += 1
		return x


myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print("-------------------------")


class MyNumbers2:
	def __iter__(self):
		self.b = 1
		return self

	def __next__(self):
		if self.b <= 20:
			y = self.b
			self.b += 1
			return y
		else:
			raise StopIteration


myclass2 = MyNumbers2()
myiter2 = iter(myclass2)

for y in myiter2:
	print(y)
