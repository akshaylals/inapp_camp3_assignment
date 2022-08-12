#!C:\Users\Akshaylal\AppData\Local\Programs\Python\Python310\python.exe

print('content-type: text/html')

import cgitb
cgitb.enable()

import cgi
import html
import os

try:
    import msvcrt
    msvcrt.setmode(0, os.O_BINARY)
    msvcrt.setmode(1, os.O_BINARY)
except ImportError:
    pass

form = cgi.FieldStorage()

name = html.escape(form.getvalue('name', ''))
email = html.escape(form.getvalue('email', ''))
password = html.escape(form.getvalue('password', ''))
emotions = form.getlist('emotion')
satisfied = form.getvalue('satisfied', '')
comments = html.escape(form.getvalue('comments'))
fileitem = form['bio']
locaiton = form.getvalue('location', '')

if fileitem.filename:
    imagename = os.path.basename(fileitem.filename)
    open('files/' + imagename, 'wb').write(fileitem.file.read())
    message = 'The file was uploaded'
    url = 'files/' + fileitem.filename
else:
    message = 'No file was uploaded'
    url = '#'


print(f'''
<html>
<head>
    <title>Feedback Form submit</title>
</head>
<body>
    Name: { name }<br>
    Email: { email }<br>
    Password: { password }<br>
    Emotions: { ", ".join([html.escape(i) for i in emotions]) }<br>
    Satisfied: { satisfied }<br>
    Comments: { comments }<br>
    Bio photo: { message }<br>
    <img src="{ url }"><br>
    Locaion visited: { locaiton }<br>
</body>
</html>
''')