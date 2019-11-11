import mysql.connector

f = open("Quiz 11.txt", "r")
print(f.read())
print("-------------------------")
f = open("Quiz 11.txt", "a")
f.write("The best way we learn anything is by practice and exercise questions")
f.close()
f = open("Quiz 11.txt", "r")
print(f.read())
print("-------------------------")

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="1234",
	database="MyEmployee"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE MyEmployee")
mycursor.execute("CREATE TABLE Employee (id INT AUTO_INCREMENT PRIMARY KEY, FirstName VARCHAR(255), "
                 "LastName VARCHAR(255), Age INT, Gender VARCHAR(255), Salary INT)")
sql = "INSERT INTO Employee (FirstName, LastName, Age, Gender, Salary) VALUES (%s, %s, %s, %s, %s)"
val = [
	("Ahmed", "Ali", 30, "Male", 10000),
	("Khalid", "Muhammad", 34, "Male", 7000),
	("Norah", "Saleh", 29, "Female", 7000)
]

mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "record was inserted.")
mycursor.execute("SELECT * FROM Employee")
myresult = mycursor.fetchall()
for x in myresult:
	print(x)
print("-------------------------")
mycursor.execute("SELECT FirstName, Gender, Salary FROM Employee")
myresult = mycursor.fetchall()
for x in myresult:
	print(x)
print("-------------------------")
sql = "SELECT * FROM Employee ORDER BY FirstName DESC"
mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
	print(x)
print("-------------------------")
sql = "DELETE FROM Employee WHERE aGE = 34"
mycursor.execute(sql)
mydb.commit()
mycursor.execute("SELECT * FROM Employee")
myresult = mycursor.fetchall()
for x in myresult:
	print(x)
