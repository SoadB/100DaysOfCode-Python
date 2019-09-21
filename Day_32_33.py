
# Test

listA = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19}
listB = {0, 2, 4, 6, 8, 10, 12, 14, 16, 18}


for x in listA:
	for y in listB:
		if x in range(3, 17) and y in range(2, 16):
			print(x, y)
