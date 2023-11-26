#!C:\Program Files (x86)\Python38-32/python.exe
print("Content-Type:text/html\n")
import pymysql

mydb = pymysql.connect(user='root',password='',host='localhost',
                                database='manohar')

mycursor = mydb.cursor()

sql = "INSERT INTO std (name, age) VALUES ('riyah','3')"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
