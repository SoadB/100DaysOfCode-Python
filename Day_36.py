

def myfun(n):
	return lambda a: a * n


mydoubler = myfun(2)
print(mydoubler(11))
print("-------------------------")

mytripler = myfun(3)
print(mytripler(11))
print("-------------------------")


def myfun(n):
	return lambda a: a * n


mydoubler = myfun(2)
mytripler = myfun(3)

print(mydoubler(11))
print(mytripler(11))

