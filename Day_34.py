
def my_function(food):
	for x in food:
		print(x)


fruits = ['apple', 'banana', 'orange']
my_function(fruits)
print("-------------------------")


def product_fun(x):
	return 5 * x


print(product_fun(2))
print(product_fun(8))
print(product_fun(11))
print("-------------------------")


def my_fun(child3, child2, child1):
	print("The youngest child is " + child3)


my_fun(child1='Ahmed', child2='Khalid', child3='Omar')
print("-------------------------")


def my_func(*kids):
	print("The youngest child is " + kids[2])


my_func ('Ahmed', 'Omar', 'Khalid')
print("-------------------------")


def tri_recursion(k):
	if k > 0:
		result = k+tri_recursion(k-1)
		print(result)
	else:
		result = 0
	return result


tri_recursion(6)
print("-------------------------")