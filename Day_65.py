
price  = 49
txt = 'The price is {} dollars'
print(txt.format(price))
print("-------------------------")

txt = 'The price is {:.2f} dollars'
print(txt.format(price))
print("-------------------------")

quantity = 3
itemno = 567
myorder = 'I want {} pieces of item number {} for {: .2f} dollars'
print(myorder.format(quantity, itemno, price))
print("-------------------------")

