#!C:\Program Files (x86)\Python38-32/python.exe
print("Content-Type:text/html\n")
import pymysql
mydb=pymysql.connect(host="localhost",user="root",password="",database="jagadeesh")
m = mydb.cursor()
m.execute("CREATE TABLE asd(name varchar(30),username varchar(30),password varchar(30),gender varchar(10),dateofbirth varchar(18),bloodgroup varchar(6),weight varchar(4),street varchar(100),area varchar(100),city varchar(100),pincode varchar(6),mobile varchar(10),email varchar(100))")
print("table created successfully")
mydb.close()
