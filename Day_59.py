
import re
txt = 'The rain is Spain'
x = re.sub("\s", "9", txt)
print(x)
print("-------------------------")

x = re.sub("\s", "9", txt, 2)
print(x)
print("-------------------------")

x = re.search(r"\bS\w+", txt)
print(x.span())
print(x.string)
print(x.group())

