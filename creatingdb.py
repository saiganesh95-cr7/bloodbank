#!C:\Program Files (x86)\Python38-32/python.exe
print("Content-Type:text/html\n")
import pymysql
bemydb=pymysql.connect(
	host="localhost",
	user="root",
	password="")

m=bemydb.cursor()
m.execute("CREATE DATABASE jagadeesh")
print("database created successfully")
