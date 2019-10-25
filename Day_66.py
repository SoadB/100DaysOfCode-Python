
price = 49
quantity = 3
itemno = 567
myorder = 'I want {0} pieces of item number {1} for {2: .2f} dollars'
print(myorder.format(quantity, itemno, price))
print("-------------------------")

age = 36
name = 'John'
txt = 'His name is: {1}. {1} is {0} years old.'
print(txt.format(age, name))
print("-------------------------")

myorder = 'I have a {carname}, it is a {model}'
print(myorder.format(carname='Ford', model='Mustang'))



