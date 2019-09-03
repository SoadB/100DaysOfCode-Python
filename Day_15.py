
# Ex1
course = ['OS', 'HCI', 'Math']
print(len(course))
print("-------------------------")
# Ex2
course.append('ENGL')
print(course)
print("-------------------------")
# Ex3
course.insert(2, 'Programming')
print(course)
print("-------------------------")
# Ex4
course.remove('Math')
print(course)
print("-------------------------")
# Ex5
course.pop()
print(course)
print("-------------------------")
# Ex6
course.pop(1)
print(course)
print("-------------------------")
# Ex7
course.clear()
print(course)
list1 = ['A', 'B', 'C']
list2 = list1.copy()
print(list2)
print("-------------------------")
# Ex8
list3 = list(list1)
print(list3)
print("-------------------------")
# Ex9
newList = list((10, 20, 50, 40, 30))
print(newList)
print("-------------------------")
# Ex10
newList.reverse()
print(newList)
newList.sort()
print(newList)
