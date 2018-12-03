import mysql.connector
from mysql.connector import errorcode

db_connection = mysql.connector.connect(user='root', password='root',
                                        host='127.0.0.1', database='School')

#mycursor = db_connection.cursor() # set cursor to read db connection

#mycursor.execute("SHOW DATABASES") # Shows list of Databases

'''List db's via for loop
for db in mycursor:
    print(db)'''

mycursor = db_connection.cursor()
mycursor.execute("CREATE TABLE Teachers (Teacher_Name VARCHAR(255), Teacher_Age TINYINT(255), Teacher_Qualification VARCHAR(255), Teacher_Experience INT(255), Teacher_Salary VARCHAR(255))")
