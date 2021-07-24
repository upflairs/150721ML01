Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
== RESTART: C:/Users/hp/Desktop/UFT/15072021ML01/day7/script_file.py ==
name,age,subject
rahul,20,python
vineetha,20,java
vinod,21,python
kajal,18,python
abhishek,19,java

{'name': ('rahul', 'vineetha', 'vinod', 'kajal', 'abhishek'), 'age': ('20', '20', '21', '18', '19'), 'subject': ('python', 'java', 'python', 'python', 'java')}
>>> # Libraries in Python
>>> import json
>>> import csv
>>> with open('new.json','w') as f:
	json.dump(d,f)
	f.close()

	
>>> with open('new.json','r') as f:
	new = json.load(f)
	f.close()

	
>>> new
{'name': ['rahul', 'vineetha', 'vinod', 'kajal', 'abhishek'], 'age': ['20', '20', '21', '18', '19'], 'subject': ['python', 'java', 'python', 'python', 'java']}
>>> with open('new.json','r') as f:
	news = json.loads(f)
	f.close()

	
Traceback (most recent call last):
  File "<pyshell#13>", line 2, in <module>
    news = json.loads(f)
  File "C:\Users\hp\AppData\Local\Programs\Python\Python39\lib\json\__init__.py", line 339, in loads
    raise TypeError(f'the JSON object must be str, bytes or bytearray, '
TypeError: the JSON object must be str, bytes or bytearray, not TextIOWrapper
>>> f
<_io.TextIOWrapper name='new.json' mode='r' encoding='cp1252'>
>>> f.close()
>>> f.read()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    f.read()
ValueError: I/O operation on closed file.
>>> 
== RESTART: C:/Users/hp/Desktop/UFT/15072021ML01/day7/script_file.py ==
ye mera function h python ka!!!!
>>> 
== RESTART: C:/Users/hp/Desktop/UFT/15072021ML01/day7/script_file.py ==
ye mera function h python ka!!!!
hahahahaha
ye mera function h python ka!!!!
>>> 
== RESTART: C:/Users/hp/Desktop/UFT/15072021ML01/day7/script_file.py ==
ye mera function h python ka!!!!
>>> k
>>> print(k)
None
>>> 
== RESTART: C:/Users/hp/Desktop/UFT/15072021ML01/day7/script_file.py ==
136
>>> 
== RESTART: C:/Users/hp/Desktop/UFT/15072021ML01/day7/script_file.py ==
>>> k
'this is the output'
>>> 
== RESTART: C:/Users/hp/Desktop/UFT/15072021ML01/day7/script_file.py ==
hahahaha
>>> 
== RESTART: C:/Users/hp/Desktop/UFT/15072021ML01/day7/script_file.py ==
1.1666666666666667
>>> 
== RESTART: C:/Users/hp/Desktop/UFT/15072021ML01/day7/script_file.py ==
(6, 27, 7)
>>> m,n,p = func6(9)
>>> m
18
>>> n
729
>>> p
13
>>> func5(x=10,z=30,y=4)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    func5(x=10,z=30,y=4)
NameError: name 'func5' is not defined
>>> 
== RESTART: C:/Users/hp/Desktop/UFT/15072021ML01/day7/script_file.py ==
1.1666666666666667
>>> func5(x=10,z=30,y=4)
0.4666666666666667
>>> func5(x=10,z=30)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    func5(x=10,z=30)
TypeError: func5() missing 1 required positional argument: 'y'
>>> 
== RESTART: C:/Users/hp/Desktop/UFT/15072021ML01/day7/script_file.py ==
3.0
>>> 
== RESTART: C:/Users/hp/Desktop/UFT/15072021ML01/day7/script_file.py ==
0
7
49
Traceback (most recent call last):
  File "C:/Users/hp/Desktop/UFT/15072021ML01/day7/script_file.py", line 86, in <module>
    func8('hi','bye','go')
  File "C:/Users/hp/Desktop/UFT/15072021ML01/day7/script_file.py", line 81, in func8
    print(sum(b))
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
== RESTART: C:/Users/hp/Desktop/UFT/15072021ML01/day7/script_file.py ==
()
(7,)
Traceback (most recent call last):
  File "C:/Users/hp/Desktop/UFT/15072021ML01/day7/script_file.py", line 87, in <module>
    func8(7)
  File "C:/Users/hp/Desktop/UFT/15072021ML01/day7/script_file.py", line 84, in func8
    c += i
TypeError: unsupported operand type(s) for +=: 'NoneType' and 'int'
>>> 
== RESTART: C:/Users/hp/Desktop/UFT/15072021ML01/day7/script_file.py ==
()
(7,)
(19, 30)
('hi', 'bye', 'go')
>>> 
== RESTART: C:/Users/hp/Desktop/UFT/15072021ML01/day7/script_file.py ==
()
(7,)
(19, 30)
('hi', 'bye', 'go')
([3, 4, 5, 6, 7],)
(3, 4, 5, 6, 7)
>>> 
== RESTART: C:/Users/hp/Desktop/UFT/15072021ML01/day7/script_file.py ==
{}
{'name': 'Sanaya'}
{'plate': 5, 'amount': 30}
>>> 