import mysql.connector
from  filling_data import scrape



mydb = mysql.connector.connect(
  host="localhost",
  user='root',
  password='divi1234567',
  database='names_and_adress'
)


print(mydb)

# mycursor = mydb.cursor()
#
# #"SELECT * FROM softuni.students;"
# #'UPDATE last_name SET last_name = Christian WHERE last_name = Char;'
# sql = "UPDATE students SET last_name = 'Christian' WHERE last_name = 'Char';"
# mycursor.execute(sql)
# mydb.commit()
# mycursor = mydb.cursor()
#
# mycursor.execute("SHOW DATABASES")
#
# for x in mycursor:
#   print(x)

mycursor = mydb.cursor()
sql = 'SELECT * FROM names_and_adress.customers'
#sql = "ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY"
#sql = "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))" creates new table
#sql ="INSERT INTO customers (name) VALUES (%s)"
#sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"

#You can also select the records that starts, includes, or ends with a given letter or phrase.Use the %  to represent wildcard characters:
#sql = "SELECT * FROM customers WHERE address LIKE '%way%'"
# Prevent SQL Injection
# When query values are provided by the user, you should escape the values.
#
# This is to prevent SQL injections, which is a common web hacking technique to destroy or misuse your database.
#
# The mysql.connector module has methods to escape query values:
# sql = "SELECT * FROM customers WHERE address = %s"
# adr = ("Yellow Garden 2", )
#sql = "SELECT * FROM customers ORDER BY name"
# sql = "DELETE FROM customers WHERE address = %s"
# adr = ('"Yellow Garden 2", ')

#mycursor.execute(sql, adr)

#mydb.commit()

#print(mycursor.rowcount, "record(s) deleted")
#mycursor.execute(sql)

#val = scrape('https://jsonplaceholder.typicode.com/users')

#mycursor.executemany(sql, val)
#mycursor.execute(sql, val)
#mydb.commit()
#print("1 record inserted, ID:", mycursor.lastrowid)
mycursor.execute(sql)
myresult = mycursor.fetchall()


for x in myresult:
  print(x)


# mycursor = mydb.cursor()
#
# mycursor.execute("CREATE DATABASE names_and_adress")