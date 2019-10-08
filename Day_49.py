
x = 300


def myfun():
	x = 200
	print(x)


myfun()
print(x)
print("-------------------------")


def myfun():
	global x
	x = 50


myfun()

print(x)
print("-------------------------")

