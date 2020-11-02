#Generate 3 months of individual pages for recently opened files

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
{h1}
</h1>
<h2>
{mystring}
</h2>
</center>
</body>
</html>
"""

for x in range(1, 31):
    title="june"+str(x)
    h1="June "+str(x)
    print(title+".html")
    f = open(title+".html", "w")
    f.write(template.format(title=title,h1=h1, mystring="No files opened on this day."))
    f.close()

for x in range(1, 32):
    title="july"+str(x)
    h1="July "+str(x)
    print(title+".html")
    f = open(title+".html", "w")
    f.write(template.format(title=title,h1=h1, mystring="No files opened on this day."))
    f.close()
    #print(template.format(title=x, mystring="No files opened on this day."))

for x in range(1, 32):
    title="august"+str(x)
    h1="August "+str(x)
    print(title+".html")
    f = open(title+".html", "w")
    f.write(template.format(title=title,h1=h1, mystring="No files opened on this day."))
    f.close()