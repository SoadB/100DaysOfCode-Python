
# Ex1
thisSet = {'OS', 'HCI', 'Math', 'Programming'}
print(len(thisSet))
print("-------------------------")

# Ex2
thisSet.remove('Math')
print(thisSet)
print("-------------------------")

thisSet.discard('Programming')
print(thisSet)
print("-------------------------")

# Ex3
x = thisSet.pop()
print(x)
print(thisSet)
print("-------------------------")

# Ex4
thisSet.clear()
print(thisSet)
print("-------------------------")

'''
 Ex5 NameError: name 'thisSet' is not defined
del thisSet
print(thisSet)
'''

# Ex6
Set1 = set(('apple', 'banana'))
print(Set1)
print("-------------------------")

