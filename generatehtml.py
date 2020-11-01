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

for x in range(1, 32):
    title="july "+str(x)
    print(title+".html")
    f = open(title+".html", "w")
    f.write(template.format(title=title, mystring="No files opened on this day."))
    f.close()
    #print(template.format(title=x, mystring="No files opened on this day."))
