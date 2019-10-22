
import json
import re

weekDays = ("Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
x = json.dumps(weekDays)
print(x)
print("-------------------------")

str = 'data is the new oil'
x = re.search("data", str)
if x:
	print("Yes, it is present")
else:
	print("No match")


