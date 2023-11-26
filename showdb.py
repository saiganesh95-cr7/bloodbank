#!C:\Program Files (x86)\Python38-32/python.exe
print("Content-Type:text/html\n")
import pymysql
mydb=pymysql.connect(
	host="localhost",
	user="root",
	password="")

m = mydb.cursor()
m.execute("SHOW DATABASES")
for db in m:
	print(db)
