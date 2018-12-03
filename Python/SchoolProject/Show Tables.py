import mysql.connector
from mysql.connector import errorcode

db_connection = mysql.connector.connect(user='root', password='root',
                                        host='127.0.0.1', database='School')

mycursor = db_connection.cursor()

mycursor.execute("SHOW TABLES")

for table in mycursor:
  print(table)
