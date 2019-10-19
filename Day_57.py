
import re

txt = 'The rain is Spain'
x = re.search("^The.*Spain$", txt)

if (x):
	print("YES! We have a match!")

else:
	print("No match")
print("-------------------------")
x = re.search("rain$", txt)
if (x):
	print("YES! We have a match!")

else:
	print("No match")
print("-------------------------")

x = re.search("\s", txt)
if (x):
	print("YES! We have a match!")

else:
	print("No match")
print("-------------------------")
x = re.search("[as]", txt)
if (x):
	print("YES! We have a match!")

else:
	print("No match")
print("-------------------------")