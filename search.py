#!C:\Program Files (x86)\Python38-32/python.exe
print("Content-Type: text/html\n\n")
import sys
import cgi, cgitb
import pymysql


mydb=pymysql.connect(host="localhost",user="root",password="",database="jagadeesh")
mycursor=mydb.cursor()
cgitb.enable() 
form=cgi.FieldStorage()
se = form.getvalue('search')
sql="SELECT * FROM asd WHERE bloodgroup=%s"
val = (se,)
mycursor.execute(sql, val)
result=mycursor.fetchall()

print('''<html>
<head>
<title>blood bank</title>
<style>
*{
margin:0;
padding:0;
}
body{
background: url("BB2.jpg");
background-position:center;
background-size: cover;

}

.icon{
color:rgb(255, 0, 0);
font-size:35px;
font-family:Serif;
padding-left:20px;
float:left;
padding-top:10px;
}


.menu{
width:400px;
float:left;
height:70px;
padding-top:100px;
}


ul{
float:left;
display:flex;
justify-content:right;
align-items:right;
}

ul li{
list-style:none;
margin-left:62px;
margin-top:12;
font-size:14px;
}
ul li a{
text-decoration:none;
color:rgb(143, 77, 201);
font-family:Serif;
font-weight:bold;
transition: 0.4s ease-in-out;
}
ul li a:hover{
color:red;
}


.search{
width:325px;
float:left;
margin-left:320px;
position:absolute;
}

.srch{
font-family: "Lucida Console";
width:320px;
height:40;
background:transparent;
border:1px solid rgb(143, 77, 201);
margin-top:25px;
color:#ff0000;
border-right:none;
font-size:16px;
float:left;
padding:10px;
border-bottom-left-radius:5px;
border-top-left-radius:5px;

}
.btn{
width:100px;
height:40px;
background:rgb(143, 77, 201);
border:2px solid rgb(143, 77, 201);
margin-top:25px;
color:#ff0000;
float:right;
position:absolute;
font-size:15px;
padding:10px;
border-bottom-right-radius:5px;
border-bottom-right-radius:5px;

}

.btn:focus{
outline:none;
}

.srch:focus{
outline:none;
}

.lg{
width:100%
}

.image{
width:100px;
height:100px;
float:left;
}
.table{
width:100%;
}




</style>
<body>
<div class = "main">
	<div class="navbar">
		<div class="icon">
			<h2 class="logo">Blood Bank</h2>
			<a href="jagadeesh1.html"><img src="blod.webp" class="image"></a>
		</div>
		<div class="menu">
			<ul>
				<li><a href="jagadeesh1.html">HOME</a></li>
				<li><a href="https://en.wikipedia.org/wiki/Blood_bank" target="_blank" >ABOUT</a></li>
				<li><a href="https://www.google.com/maps/search/nearest+blood+bank+to+my+location/@16.2389046,80.0354258,14z" target="_blank">SERVICE</a></li>
				<li><a href="https://indianhelpline.com/BLOOD-BANKS/" target="_blank">CONTACT</a></li>
				<li><a href="new 1.html">BLOOD TYPES</a></li>
			</ul>
		</div>
		<div class="search">
                        <form action='search.py' method='POST' class='search'>
			<input class="srch" type="search" name="search" placeholder="type your blood group"aria-label='Search through site content'>
			<button type="submit" class="btn">Search</button>
			</form>
			
		</div>

	</div>
</div>
		<div class="table">
		    <table class="tlb" style='border:1px solid black;margin-left:0;margin-top:160;'>
                    <tr>
                    <th style='border:1px solid;'><b>name</b></th>&nbsp&nbsp
                    <th style='border:1px solid;'><b>username</b></th>&nbsp&nbsp
                    <th style='border:1px solid;'><b>gender</b></th>&nbsp&nbsp
                    <th style='border:1px solid;'><b>dateofbirth</b></th>&nbsp&nbsp
                    <th style='border:1px solid;'><b>bloodgroup</b></th>&nbsp&nbsp
                    <th style='border:1px solid;'><b>weight</b></th>&nbsp&nbsp
                    <th style='border:1px solid;'><b>street</b></th>&nbsp&nbsp
                    <th style='border:1px solid;'><b>area</b></th>&nbsp&nbsp
                    <th style='border:1px solid;'><b>city</b></th>&nbsp&nbsp
                    <th style='border:1px solid;'><b>pincode</b></th>&nbsp&nbsp
                    <th style='border:1px solid;'><b>mobile</b></th>&nbsp&nbsp
                    <th style='border:1px solid;'><b>email</b></th></tr>&nbsp&nbsp''')

for rows in result:
    i=0
    for r in rows:
    
        print("<tr><td style='border:1px solid black;'>",r,end='',sep=''"</td></tr>")
        
        
        print("</table>")
 
    print("<table border=2px solid black>")
    print("<tr><td>name</td><td>",rows[i],"</td></tr>")
    print("</table>")
   
 

