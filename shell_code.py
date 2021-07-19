Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 10
>>> type(a)
<class 'int'>
>>> # String
>>> s = 'Hello it is python'
>>> type(s)
<class 'str'>
>>> len(s)
18
>>> print(s)
Hello it is python
>>> s
'Hello it is python'
>>> s1 = "Hello it is python"
>>> s2 = 'i am trying to write multiple lines
SyntaxError: EOL while scanning string literal
>>> s2 = 'i am trying to write multiple lines'
>>> s2 = '''i am trying to write multiple lines
and i could make it possible
like i used to do
earlier as well'''
>>> s3 = """i am trying to write multiple lines
and i could make it possible
like i used to do
earlier as well"""
>>> type(s1)
<class 'str'>
>>> type(s2)
<class 'str'>
>>> type(s3)
<class 'str'>
>>> print(s1)
Hello it is python
>>> s1
'Hello it is python'
>>> s2
'i am trying to write multiple lines\nand i could make it possible\nlike i used to do\nearlier as well'
>>> print(s2)
i am trying to write multiple lines
and i could make it possible
like i used to do
earlier as well
>>> s3
'i am trying to write multiple lines\nand i could make it possible\nlike i used to do\nearlier as well'
>>> print(s3)
i am trying to write multiple lines
and i could make it possible
like i used to do
earlier as well
>>> 'd:\'
SyntaxError: EOL while scanning string literal
>>> 'd:\\'
'd:\\'
>>> print('d:\\')
d:\
>>> # operations on string
>>> # item accessing
>>> s
'Hello it is python'
>>> s[0]
'H'
>>> s[4]
'o'
>>> s[len(s)-1]
'n'
>>> s[-1]
'n'
>>> s[-6]
'p'
>>> #slicing
>>> s[0:5:1]
'Hello'
>>> s[0:5:2]
'Hlo'
>>> len(s)
18
>>> s[-18:5:1]
'Hello'
>>> s[0:-13:1]
'Hello'
>>> s[-18:-13:1]
'Hello'
>>> s[-13:-18:1]
''
>>> s[-13:-18:-1]
' olle'
>>> s[-14:-19:-1]
'olleH'
>>> s[4:0:-1]
'olle'
>>> s[4:-19:-1]
'olleH'
>>> s[0:5:]
'Hello'
>>> s[0:5]
'Hello'
>>> s[:5]
'Hello'
>>> s[-6:18:1]
'python'
>>> s[-6:18]
'python'
>>> s[-6:]
'python'
>>> s
'Hello it is python'
>>> s[-1:-10:-1\]
  
SyntaxError: unexpected character after line continuation character
>>> s[-1:-10:-1]
'nohtyp si'
>>> s[:-10:-1]
'nohtyp si'
>>> s[4::-1]
'olleH'
>>> s[::-1]
'nohtyp si ti olleH'
>>> 