#Generates page that links to all the weekly outgoing email data and generates each individual weeks page

template = """
<html>
<head>
<title>{title}</title>
<link rel="stylesheet" href="hack.css">
<link rel="stylesheet" href="style.css">
</head>
<body>
<center>
<h1>
{title}
</h1>
<h2>
{mystring}
</h2>
</center>
</body>
</html>
"""

message=""

for x in range(1, 14):
    message=message+"<a href=""{url}.html"">{body}</a><br>".format(url="/emailoutgoingdata/week"+str(x), body="Week "+str(x))


f = open("outgoingemaildata.html", "w")
f.write(template.format(title="Outgoing Email Data", mystring=message))
f.close()

for x in range(1, 14):
    f = open("week"+str(x)+".html", "w")
    f.write(template.format(title="Week "+str(x)+" Outgoing Email Data", mystring='<img src="week'+str(x)+'.png">'))
    f.close()