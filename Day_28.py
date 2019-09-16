
# Ex1
i = 1
while i < 6:
	print(i)
	i += 1
print("-------------------------")

# Ex2
i = 1
while i <= 5:
	print(i)
	if i == 4:
		break
	i += 1
print("-------------------------")

# Ex3
i = 0
while i < 6:
	i += 1
	if i == 3:
		continue
	print(i)
print("-------------------------")

# Ex4
i = 1
while i < 6:
	print(i)
	i += 1
else:
	print("i is longer than 5")
print("-------------------------")