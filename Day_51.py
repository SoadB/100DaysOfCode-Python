
import mymodule_Day_50 as mx
from mymodule_Day_50 import person1
import platform

a = mx.person1['age']
print(a)
print("-------------------------")

x = platform.system()
print(x)
print("-------------------------")

print(platform.python_version())
print("-------------------------")

y = dir(platform)
print(y)
print("-------------------------")

print(person1['age'])


