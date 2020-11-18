#Generate 3 months of individual pages for recently opened files
import random

def getFile():
    r=random.randint(0, 5)
    if r==1:
        return "No files opened on this date"
    elif r==2:
         return "No files opened on this date"
    elif r==3:
        return "Demon Days.mp3"
    elif r==4:
        return "Demon Days.mp3"
    elif r==5:
        return "lessonplan.txt"
    

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
    f.write(template.format(title=title,h1=h1, mystring=getFile()))
    f.close()

for x in range(1, 32):
    title="july"+str(x)
    h1="July "+str(x)
    print(title+".html")
    f = open(title+".html", "w")
    f.write(template.format(title=title,h1=h1, mystring=getFile()))
    f.close()
    #print(template.format(title=x, mystring="No files opened on this day."))

for x in range(1, 32):
    title="august"+str(x)
    h1="August "+str(x)
    print(title+".html")
    f = open(title+".html", "w")
    f.write(template.format(title=title,h1=h1, mystring=getFile()))
    f.close()