#!C:\Program Files (x86)\Python38-32/python.exe
print("Content-Type:text/html\n")
import cgi, cgitb
import pymysql
cgitb.enable() 
import sys
form=cgi.FieldStorage()

na= form.getvalue('name')
x = form.getvalue('username')
z = form.getvalue('password')
ag= form.getvalue('gender')
q = form.getvalue('datepicker1')
w = form.getvalue('bloodgroup')
e = form.getvalue('weight')
r = form.getvalue('street')
t = form.getvalue('area')
y = form.getvalue('city')
u = form.getvalue('pincode')
i = form.getvalue('mobile')
o = form.getvalue('email')
con=pymysql.connect(user='root',password='',host='localhost',
                                database='jagadeesh')
cur=con.cursor()
sql = "INSERT INTO asd (name,username,password,gender,dateofbirth,bloodgroup,weight,street,area,city,pincode,mobile,email) VALUES(%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s)"
val = (na,x,z,ag,q,w,e,r,t,y,u,i,o)
cur.execute(sql, val)
con.commit()
con.close()
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

.sign{
float:left;
margin-left:770px;
position:absolute;
}

.sgin{
width:100px;
height:40px;
background:rgb(143, 77, 201);
border:2px solid rgb(143, 77, 201);
margin-top:25px;
color:#ff0000;
font-size:15px;
padding:10px;
border-bottom-right-radius:5px;
border-bottom-right-radius:5px;
}

div button:hover{
color:#fff;
}


input[type=text], input[type=password] {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  box-sizing: border-box;
}

button {
width:100px;
height:40px;
background:rgb(143, 77, 201);
border:2px solid rgb(143, 77, 201);
margin-top:25px;
color:#ff0000;
font-size:15px;

padding:10px;
border-bottom-right-radius:5px;
border-bottom-right-radius:5px;
}

div button:hover{
color:#fff;
}


.cancelbtn {
  width: auto;
  padding: 10px 18px;
  background-color: rgb(143, 77, 201);
}


.imgcontainer {
  text-align: center;
  margin: 24px 0 12px 0;
  position: relative;
}

img.avatar {
  width: 40%;
  border-radius: 50%;
}

.container {
  padding: 16px;
}

span.psw {
  float: right;
  padding-top: 16px;
}


.modal {
  display: none; 
  position: fixed; 
  z-index: 1; 
  left: 0;
  top: 0;
  width: 100%; 
  height: 100%; 
  overflow: auto; 
  background-color: rgb(0,0,0); 
  background-color: rgba(0,0,0,0.4);
  padding-top: 60px;
}


.modal-content {
  background-color: #fefefe;
  margin: 5% auto 15% auto; /* 5% from the top, 15% from the bottom and centered */
  border: 1px solid #888;
  width: 80%; /* Could be more or less, depending on screen size */
}


.close {
  position: absolute;
  right: 25px;
  top: 0;
  color: #000;
  font-size: 35px;
  font-weight: bold;
}

.close:hover,
.close:focus {
  color: red;
  cursor: pointer;
}


.animate {
  -webkit-animation: animatezoom 0.6s;
  animation: animatezoom 0.6s
}

@-webkit-keyframes animatezoom {
  from {-webkit-transform: scale(0)} 
  to {-webkit-transform: scale(1)}
}
  
@keyframes animatezoom {
  from {transform: scale(0)} 
  to {transform: scale(1)}
}


@media screen and (max-width: 300px) {
  span.psw {
     display: block;
     float: none;
  }
  .cancelbtn {
     width: 100%;
  }
}


.lg{
width:100%
}

.image{
width:100px;
height:100px;
float:left;
}

</style>
<body>
<div class = "main">
	<div class="navbar">
		<div class="icon">
			<h2 class="logo">Blood Bank</h2>
			<a href="jagadeesh.html"><img src="blod.webp" class="image"></a>
		</div>
		<div class="menu">
			<ul>
				<li><a href="jagadeesh.html">HOME</a></li>
				<li><a href="https://en.wikipedia.org/wiki/Blood_bank" target="_blank" >ABOUT</a></li>
				<li><a href="https://www.google.com/maps/search/nearest+blood+bank+to+my+location/@16.2389046,80.0354258,14z" target="_blank">SERVICE</a></li>
				<li><a href="https://indianhelpline.com/BLOOD-BANKS/" target="_blank">CONTACT</a></li>
				<li><a href="new 1.html">BLOOD TYPES</a></li>
			</ul>
		</div>
		<div class="search">
			<input class="srch" type="search" name="" placeholder="type your blood group">
			<a href="#"><button class="btn">Search</button></a>
			
		</div>
		<div class="sign">
			<button class="sgin" onclick="window.location.href='BDI2.html';">sign in</button>
			<button class="login" onclick="document.getElementById('id01').style.display='block'" style="width:auto;">Login</button>

			<div id="id01" class="modal">
  
  			<form class="modal-content animate" action="/action_page.php" method="post">
    		<div class="imgcontainer">
      	<span onclick="document.getElementById('id01').style.display='none'" class="close" title="Close Modal">&times;</span>
      	<img src="bl.jpg" alt="Avatar" class="avatar">
    		</div>

    		<div class="container">
      	<label for="uname"><b>Username</b></label>
      	<input type="text" placeholder="Enter Username" name="uname" required>

      	<label for="psw"><b>Password</b></label>
      	<input type="password" placeholder="Enter Password" name="psw" required>
        
      	<button type="submit" class="lg">Login</button>
      	<label>
        <input type="checkbox" checked="checked" name="remember"> Remember me
      	</label>
    		</div>

    		<div class="container" style="background-color:#f1f1f1">
      	<button type="button" onclick="document.getElementById('id01').style.display='none'" class="cancelbtn">Cancel</button>
      	<span class="psw">Forgot <a href="#">password?</a></span>
    		</div>
  			</form>
			</div>

			<script>
			var modal = document.getElementById('id01');

			window.onclick = function(event) {
    		if (event.target == modal) {
        modal.style.display = "none";
    			}
			}
			</script>
			</div>
		</div>
	</div>	
</body>
</html>
''')



