
# Ex1
thisdic = {'brand': 'Ford',
           'model': 'Mustang',
           'year': 1964}
if 'model' in thisdic:
    print('Yes')
print("-------------------------")

# Ex2
print(len(thisdic))
print("-------------------------")

# Ex3
thisdic['color'] = 'red'
print(thisdic)
print("-------------------------")

# Ex4
thisdic.pop('model')
print(thisdic)
print("-------------------------")

# Ex5
thisdic.popitem()
print(thisdic)
print("-------------------------")

# Ex6
del thisdic['brand']
print(thisdic)
print("-------------------------")

# Ex7
thisdic.clear()
print(thisdic)
print("-------------------------")