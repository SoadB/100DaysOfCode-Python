
# Test
S = "Please, I want {} sandwiches and {} donutes"

S = S.replace("I", "we")
S = S.format(5, 7)

for i in S:
	if i == 'a':
		i = i.upper()
		S = S.replace('a', i)

print("\n"+S)



