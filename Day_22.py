# Ex1
thisdic = {'brand': 'Ford',
           'model': 'Mustang',
           'year': 1964}
print(thisdic)
print("-------------------------")
# Ex2
x = thisdic['model']
print(x)
y = thisdic.get('brand')
print(y)
print("-------------------------")
# Ex3
thisdic['year'] = 2018
print(thisdic)
print("-------------------------")
# Ex4
for x in thisdic:
    print(x)
print("-------------------------")
# Ex5
for x in thisdic:
    print(thisdic[x])
print("-------------------------")
# Ex6
for x in thisdic.values():
    print(x)
print("-------------------------")
# Ex7
print(thisdic.values())
print("-------------------------")
# Ex8
for x, y in thisdic.items():
    print(x, y)
print("-------------------------")
# Ex9
print(thisdic.items())
