
import json

# some JSON:
x = '{ "name" : "John", "age" : 30, "city" : "New York"}'

# parse x:
y = json.loads(x)

# the result a python dictionary:
print(y["age"])
print("-------------------------")

# a python object
x = {"name": "John",
     "age": 30,
     "city": "New York"
     }
# convert into JSON :
y = json.dumps(x)
# the result is JSON string:
print(y)
print("-------------------------")

print(json.dumps({"name" : "John", "age" : 30}))
print(json.dumps(["apple", "banana"]))
print(json.dumps(("apple", "banana")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
print("-------------------------")

s = {
 "name": "John",
 "age": 30,
 "married": True,
 "divorced": False,
 "children": ("Ann", "Billy"),
 "pets": None,
 "cars": [
  {"model": "BMW 230", "mpg": 27.5},
  {"model": "Ford Edge", "mpg": 24.1}
 ]
    }
# convert into JSON
w = json.dumps(s)
print(w)
