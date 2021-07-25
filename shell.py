Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
== RESTART: C:/Users/hp/Desktop/UFT/15072021ML01/day8/script_file.py ==
Hi I am a function
>>> 
== RESTART: C:/Users/hp/Desktop/UFT/15072021ML01/day8/script_file.py ==
27000
>>> 
== RESTART: C:/Users/hp/Desktop/UFT/15072021ML01/day8/script_file.py ==
Ok
wow
>>> 
== RESTART: C:/Users/hp/Desktop/UFT/15072021ML01/day8/script_file.py ==
nice
>>> 
== RESTART: C:/Users/hp/Desktop/UFT/15072021ML01/day8/script_file.py ==
8
>>> 
== RESTART: C:/Users/hp/Desktop/UFT/15072021ML01/day8/script_file.py ==
8
>>> 
== RESTART: C:/Users/hp/Desktop/UFT/15072021ML01/day8/script_file.py ==
[13, 14, 28, 30, 19, 44, 77, 13, 16, 12, 46, 18, 31, 16, 19]
[1, 2, 9, 10, 4, 17, 33, 1, 3, 1, 18, 4, 10, 3, 4]
[6, 2, 9, 10, 18, 17, 134, 6, 3, 1, 18, 4, 42, 3, 18]
>>> a
[3, 4, 18, 20, 9, 34, 67, 3, 6, 2, 36, 8, 21, 6, 9]
>>> list(map(lambda n:n-10, a))
[-7, -6, 8, 10, -1, 24, 57, -7, -4, -8, 26, -2, 11, -4, -1]
>>> map(lambda n:n-10, a)
<map object at 0x000001DBE27F4370>
>>> list(filter(lambda n:n%2==1, a))
[3, 9, 67, 3, 21, 9]
>>> a
[3, 4, 18, 20, 9, 34, 67, 3, 6, 2, 36, 8, 21, 6, 9]
>>> 
== RESTART: C:/Users/hp/Desktop/UFT/15072021ML01/day8/script_file.py ==
10
15
10
>>> 
== RESTART: C:/Users/hp/Desktop/UFT/15072021ML01/day8/script_file.py ==
10
15
15
>>> 
== RESTART: C:/Users/hp/Desktop/UFT/15072021ML01/day8/script_file.py ==
10
10
15
15
>>> 
== RESTART: C:/Users/hp/Desktop/UFT/15072021ML01/day8/script_file.py ==
10
Traceback (most recent call last):
  File "C:/Users/hp/Desktop/UFT/15072021ML01/day8/script_file.py", line 88, in <module>
    xyz()
  File "C:/Users/hp/Desktop/UFT/15072021ML01/day8/script_file.py", line 83, in xyz
    print(a)
UnboundLocalError: local variable 'a' referenced before assignment
>>> 
== RESTART: C:/Users/hp/Desktop/UFT/15072021ML01/day8/script_file.py ==
10
10
15
15
>>> 
== RESTART: C:/Users/hp/Desktop/UFT/15072021ML01/day8/script_file.py ==
10
10
15
10
>>> 
== RESTART: C:/Users/hp/Desktop/UFT/15072021ML01/day8/script_file.py ==
10
Traceback (most recent call last):
  File "C:/Users/hp/Desktop/UFT/15072021ML01/day8/script_file.py", line 123, in <module>
    xyz()
  File "C:/Users/hp/Desktop/UFT/15072021ML01/day8/script_file.py", line 117, in xyz
    print(a)
UnboundLocalError: local variable 'a' referenced before assignment
>>> 
== RESTART: C:/Users/hp/Desktop/UFT/15072021ML01/day8/script_file.py ==
10
15
30
10
>>> 
== RESTART: C:/Users/hp/Desktop/UFT/15072021ML01/day8/script_file.py ==
10 Direct
15
30
10 Direct
>>> 
== RESTART: C:/Users/hp/Desktop/UFT/15072021ML01/day8/script_file.py ==
10 Direct
15
30
20
10 Direct
>>> 
== RESTART: C:/Users/hp/Desktop/UFT/15072021ML01/day8/script_file.py ==
10 Direct
30
20
Traceback (most recent call last):
  File "C:/Users/hp/Desktop/UFT/15072021ML01/day8/script_file.py", line 125, in <module>
    xyz()
  File "C:/Users/hp/Desktop/UFT/15072021ML01/day8/script_file.py", line 120, in xyz
    a = 15 + z
NameError: name 'z' is not defined
>>> 
== RESTART: C:/Users/hp/Desktop/UFT/15072021ML01/day8/script_file.py ==
10 Direct
30
20
65
10 Direct
>>> a = [4,65,87,7,4,9,0,56,]
>>> m = map(lambda x:x*2, a)
>>> m
<map object at 0x000001A32D194CA0>
>>> next(m)
8
>>> next(m)
130
>>> next(m)
174
>>> next(m)
14
>>> next(m)
8
>>> next(m)
18
>>> next(m)
0
>>> next(m)
112
>>> next(m)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    next(m)
StopIteration
>>> next(m)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    next(m)
StopIteration
>>> m = map(lambda x:x*2, a)
>>> list(m)
[8, 130, 174, 14, 8, 18, 0, 112]
>>> list(m)
[]
>>> m = map(lambda x:x*2, a)
>>> for i in m:
	print(i)

	
8
130
174
14
8
18
0
112
>>> list(m)
[]
>>> next(m)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    next(m)
StopIteration
>>> m = map(lambda x:x*2, a)
>>> next(m)
8
>>> list(m)
[130, 174, 14, 8, 18, 0, 112]
>>> def mygen(n):
	for i in range(1,11):
		yield n*i

		
>>> nn = mygen(10)
>>> nn
<generator object mygen at 0x000001A32B04F0B0>
>>> next(nn)
10
>>> next(nn)
20
>>> list(nn)
[30, 40, 50, 60, 70, 80, 90, 100]
>>> pp = (12*i for i in range(1,5))
>>> pp
<generator object <genexpr> at 0x000001A32D1A4C80>
>>> list(pp)
[12, 24, 36, 48]
>>> list(nn)
[]
>>> list(pp)
[]
>>> 