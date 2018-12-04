import mysql.connector
from mysql.connector import errorcode

db_connection = mysql.connector.connect(user='root', password='root',
                                        host='127.0.0.1', database='School')

mycursor = db_connection.cursor()

mycursor.execute("CREATE TABLE Teachers (Teacher_ID INT(11) AUTO_INCREMENT PRIMARY KEY, Teacher_Name VARCHAR(255), Teacher_Age TINYINT(255), Teacher_Qualification VARCHAR(255), Teacher_Experience INT(255), Teacher_Salary VARCHAR(255))")
mycursor.execute("CREATE TABLE Students (Student_ID INT AUTO_INCREMENT PRIMARY KEY, Student_Name VARCHAR(255), Student_Age TINYINT(255), Student_Class INT(255), Student_Section VARCHAR(255))")

'''
import mysql.connector
from mysql.connector import errorcode

db_connection = mysql.connector.connect(user='root', password='root',
                                        host='127.0.0.1', database='School')

mycursor = db_connection.cursor()

sql_stmt = "ALTER TABLE Teachers AUTO_INCREMENT=1"
mycursor.execute(sql_stmt)

'''
