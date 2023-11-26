#!C:\Program Files (x86)\Python38-32/python.exe
print("Content-Type:text/html\n")

import pymysql
mydb=pymysql.connect(host="localhost",user="root",password="",database="jagadeesh")
mycursor=mydb.cursor()

mycursor.execute("select * from cse")
result=mycursor.fetchall()
print("<table border='1'>")
for rows in result:
    print("<tr><td>")
    print(rows)
    print("</td></tr>")
print("</table>")
