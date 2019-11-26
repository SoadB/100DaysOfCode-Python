from flask import Flask
from flask import request
from flask import render_template
from flaskext.mysql import MySQL


app = Flask(__name__)


app.config['MYSQL_DATABASE_HOST'] = 'sql12.freemysqlhosting.net'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'sql12313208'

mysql = MySQL()
mysql.init_app(app)

@app.route("/order", methods=['GET', 'POST'])


def order():
  cursor = mysql.get_db().cursor()

  if request.method == 'POST':
    type_product = request.form['type_product']
  else:
    type_product = ""

  cursor.execute('select * from products where type_name="'+str(type_product)+'"')
  result = cursor.fetchall()

  if request.method == 'POST' and "product_id" in request.form:

    product_id = request.form['product_name']
    quantity = request.form['number']

    cursor.execute('select price from products where prod_name= "'+str(product_id)+'"')

    cursor.execute("INSERT INTO orders(product_id, quantity) VALUES (%s, %s)",
                     (product_id, quantity))
    mysql.get_db().commit()



  return render_template("Order.html", title="Order", result=result)

if __name__ == "__main__":
  app.run(debug=True)





