
import re

txt = 'The rain is Spain'
x = re.findall("ai", txt)
print(x)
print("-------------------------")

x = re.findall("Portugal", txt)
print(x)
if x:
	print("YES!, there is at least one match")
else:
	print("No match")
print("-------------------------")

y = re.search("\s", txt)
print("The first white-space character is located in position:", y.start())
print("-------------------------")

y = re.search("Portugal", txt)
print(y)
print("-------------------------")

w = re.split("\s", txt)
print(w)
print("-------------------------")

