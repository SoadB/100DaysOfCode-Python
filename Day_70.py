import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="1234"
	)
print(mydb)

mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE mydatabase2")

print("-------------------------")
mycursor.execute("SHOW DATABASES")
for x in mycursor:
	print(x)

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="1234",
	database="mydatabase2"
	)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
print("-------------------------")
mycursor.execute("SHOW TABLES")
for x in mycursor:
	print(x)

mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")


