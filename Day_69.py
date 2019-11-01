
import os
f = open("demofile.txt", "r")
# print(f.read())
print(f.read(5))
print("-------------------------")
print(f.readline())
print(f.readline())
print("-------------------------")
for x in f:
	print(x)
print("-------------------------")
f.close()
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()
f = open("demofile2.txt", "r")
print(f.read())
print("-------------------------")
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()
f = open("demofile3.txt", "r")
print(f.read())
print("-------------------------")

f = open("myfile.txt", "w")


