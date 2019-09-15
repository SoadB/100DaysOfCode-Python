# Ex1
a = 50
b = 73
if b > a:
	print("b is greater than a")
print("-------------------------")

# Ex2
a = 22
b = 22
if b < a:
	print("b is greater than a")
elif a == b:
	print("a and b are equal ")
print("-------------------------")

# Ex3
a = 22
b = 40
if b < a:
	print("b is greater than a")
elif a == b:
	print("a and b are equal ")
else:
	print("b is grater than a")
print("-------------------------")

# Ex4
x = 200
y = 50
if y < x: print("x is greater than y")
print("-------------------------")

# Ex5
a = 2
b = 300
print("A") if a > b else print("B")
print("-------------------------")

# Ex6
x = 6
y = 6
print("x") if x > y else print("=") if x == y else print("y")
print("-------------------------")

# Ex7
a = 70
b = 59
c = 100
if a > b and a < c:
	print("Both conditions are true")
print("-------------------------")

# Ex8
a = 200
b = 33
c = 500
if a > b or a > c:
	print("At least one of the conditions is true")
print("-------------------------")

# Ex9
x = 41
if x > 10:
	print("above ten, ")
	if x > 20:
		print("and also above 20")
	else:
		print("but not above 20.")
print("-------------------------")