

def myfun():
	x = 300
	print(x)
myfun()
print("-------------------------")


def myfun():
	x = 200

	def myinnerfun():
		print(x)
	myinnerfun()

myfun()
print("-------------------------")

x = 50

def myfun():
	print(x)

myfun()
print(x)
print("-------------------------")


