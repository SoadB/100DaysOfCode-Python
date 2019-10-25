
try:
	print(x)
except:
	print("An exception occurred")
print("-------------------------")

try:
	print(x)
except NameError:
	print("Variable x is not defined")
except:
	print("Something else went wrong")
print("-------------------------")

try:
	print("Hello")
except:
	print("Something else went wrong")
else:
	print("Nothing went wrong")
print("-------------------------")

try:
	print(x)
except:
	print("Something else went wrong")
finally:
	print("The 'try except' is finished")


