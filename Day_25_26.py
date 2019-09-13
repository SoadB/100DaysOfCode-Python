
# test1
setNumbers = {1, 3, 5, 7, 8}
print(setNumbers)
print("-------------------------")

setNumbers.update([4, 8, 12])
print(setNumbers)
print("-------------------------")

setNumbers.remove(8)
print(setNumbers)
print("-------------------------")

setNumbers.clear()
print(setNumbers)
print("-------------------------")

# test 2
Dic = {'name': 'pigeon'
       , 'type': 'bird'
       , 'skin cover': 'feathers'}
print(Dic)
print("-------------------------")

print(Dic.get('type'))
print("-------------------------")

Dic['skin cover'] = 'Silicone'
print(Dic)
