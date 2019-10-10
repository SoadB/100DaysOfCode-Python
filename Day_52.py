
import datetime

x = datetime.datetime.now()
print(x)
print("-------------------------")

print(x.year)
print(x.strftime("%A"))
print("-------------------------")

y = datetime.datetime(2020, 5, 17)
print(y)
print("-------------------------")

print(y.strftime("%B"))
print("-------------------------")