
# Test1
LabTops = ['HP', 'DELL', 'SONY', 'MAC']
print(LabTops.count('SONY'))
print("-------------------------")

LabTops.insert(1, 'LENOVO')
print(LabTops)
print("-------------------------")

LabTops.reverse()
print(LabTops)
print("-------------------------")

LabTops.sort()
print(LabTops)
print("-------------------------")

# Test2
Tuple = ('java', 'python', 'swift')
if 'python' in Tuple:
	print('Yes')
else:
	print('No')