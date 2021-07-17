Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 3*3
9
>>> 
== RESTART: C:/Users/hp/Desktop/UFT/15072021ML01/day2/another_prog.py =
40
>>> a  =20
>>> a1=20
>>> a#2 = 30
20
>>> a$a = 40
SyntaxError: invalid syntax
>>> 1a = 30
SyntaxError: invalid syntax
>>> for = 30
SyntaxError: invalid syntax
>>> A = 30
>>> A = 40
>>> a
20
>>> A
40
>>> first_value = 50
>>> _a = 760
>>> _ = 30
>>> _
30
>>> a = b = 4
>>> a
4
>>> b
4
>>> a,b,c=6,7,8
>>> a
6
>>> b
7
>>> c
8
>>> a = 30; b='hello'
>>> a
30
>>> b
'hello'
>>> d = ((a*c)/((a+c)*9))-((a*c)/((a+c)*19))+((a*c)/((a+c)*3))
>>> d
2.47460757156048
>>> d = ((a*c)/((a+c)*9))-((a*c)/((a+c)*19))+((a*c)/((a+c)*3)) \
    + ((a*2*c)/((a-c)*9))
>>> d
4.898849995802904
>>> from keyword import kwlist
>>> kwlist
['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> len(kwlist)
36
>>> 5/2
2.5
>>> 4/2
2.0
>>> 5//2
2
>>> 4//2
2
>>> a=10
>>> a += 3
>>> a
13
>>> #a = a+3
>>> 7>3
True
>>> 8<=4
False
>>> 8==3
False
>>> (7>3) and (5<=3)
False
>>> (7>3) or (5<=3)
True
>>> (7>3) and not(5<=3)
True
>>> 6&3
2
>>> 6|3
7
>>> 6^3
5
>>> 6<<3
48
>>> 6>>3
0
>>> 6 and 3
3
>>> 6 and 4
4
>>> 6 or 4
6
>>> 48>>2
12
>>> 'help' in 'would you like to help me out'
True
>>> 'kill' in 'would you like to help me out'
False
>>> 'kill' not in 'would you like to help me out'
True
>>> 'k' in 'kite'
True
>>> a = 10
>>> b = 20
>>> c= 10
>>> type(a)
<class 'int'>
>>> id(a)
2462813809232
>>> id(b)
2462813809552
>>> id(c)
2462813809232
>>> a is c
True
>>> a is not c
False
>>> a is b
False
>>> 