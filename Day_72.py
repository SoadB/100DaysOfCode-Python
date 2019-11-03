
import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="1234",
	database="mydatabase2"
	)
mycursor = mydb.cursor()
sql = "SELECT * FROM customers ORDER BY name"
mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
	print(x)
print("-------------------------")

sql = "SELECT * FROM customers ORDER BY name DESC"
mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
	print(x)
print("-------------------------")

sql = "DELETE FROM customers WHERE address = 'Mountain 21' "
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "records deleted ")

print("-------------------------")

sql = "DROP TABLE IF EXISTS customers"
mycursor.execute(sql)
