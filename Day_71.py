import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="1234",
	database="mydatabase2"
	)
mycursor = mydb.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val =("John", "Highway 21")

mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
print("-------------------------")
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
	("John", "Highway 21"),
	("Peter", "Lowstreet 4"),
	("Amy", "Apple st 652"),
	("Hannah", "Mountain 21"),
	("John", "Highway 21"),
	("Peter", "Lowstreet 4"),
	("Amy", "Apple st 652"),
	("Hannah", "Mountain 21"),
	("John", "Highway 21"),
	("Peter", "Lowstreet 4"),
	("Amy", "Apple st 652"),
	("Hannah", "Mountain 21"),
	("Hannah", "Mountain 21")
	]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "record was inserted.")
print("-------------------------")
print("1 record inserted, ID:", mycursor.lastrowid)
print("-------------------------")
'''mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
	print(x)
print("-------------------------")
mycursor.execute("SELECT name, address FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
	print(x)
print("-------------------------")
myresult = mycursor.fetchone()
print(myresult)
sql = "SELECT * FROM customers WHERE address = 'Mountain 21'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
	print(x)'''
sql = "SELECT * FROM customers WHERE address like '%way%'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
	print(x)
