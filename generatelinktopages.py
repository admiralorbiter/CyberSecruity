template = """
<html>
<head>
<title>{title}</title>
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

for x in range(1, 31):
    message=message+"<a href=""{url}.html"">{body}</a><br>".format(url="/recentlyopenedfiles/june"+str(x), body="June "+str(x))

for x in range(1, 32):
    message=message+"<a href=""{url}.html"">{body}</a><br>".format(url="/recentlyopenedfiles/july"+str(x), body="July "+str(x))

for x in range(1, 32):
    message=message+"<a href=""{url}.html"">{body}</a><br>".format(url="/recentlyopenedfiles/august"+str(x), body="August "+str(x))

f = open("recentlyopenedfiles.html", "w")
f.write(template.format(title="Recently Opened Files", mystring=message))
f.close()