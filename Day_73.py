
import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="1234",
	database="mydatabase2"
	)
mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
	("John", "Highway 21"),
	("Peter", "Lowstreet 4")
]
mycursor.executemany(sql, val)
sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Lowstreet 4' "
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "records affected")
print("-------------------------")

mycursor.execute("SELECT * FROM customers LIMIT 3")
myresult = mycursor.fetchall()

for x in myresult:
	print(x)
print("-------------------------")

mycursor.execute("SELECT * FROM customers LIMIT 3 OFFSET 1")
myresult = mycursor.fetchall()

for x in myresult:
	print(x)
print("-------------------------")

sql = "SELECT \
      users.name AS user, \
      products.name AS favorite \
      FROM users \
      INNER JOIN products ON users.fav = products.id"
sql = "SELECT \
      users.name AS user, \
      products.name AS favorite \
      FROM users \
      LEFT JOIN products ON users.fav = products.id"
sql = "SELECT \
      users.name AS user, \
      products.name AS favorite \
      FROM users \
      RIGHT JOIN products ON users.fav = products.id"