Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Type Casting
>>> a = 10
>>> b = 20.9
>>> c = 3+4j
>>> d = '45'
>>> e = '36.3'
>>> int(b)
20
>>> int(d)
45
>>> int('sh34')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    int('sh34')
ValueError: invalid literal for int() with base 10: 'sh34'
>>> int(e)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    int(e)
ValueError: invalid literal for int() with base 10: '36.3'
>>> float(a)
10.0
>>> float(c)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    float(c)
TypeError: can't convert complex to float
>>> int(c)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    int(c)
TypeError: can't convert complex to int
>>> float(d)
45.0
>>> float(e)
36.3
>>> eval(d)
45
>>> eval(e)
36.3
>>> print('hi')
hi
>>> k = input('Enter your age:')
Enter your age:29
>>> k
'29'
>>> type(k)
<class 'str'>
>>> print 'hi'
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hi')?
>>> age = eval(input('Enter your age:'))
Enter your age:29.1
>>> age
29.1
>>> type(age)
<class 'float'>
>>> 
>>> complex(a)
(10+0j)
>>> complex(b)
(20.9+0j)
>>> complex(d)
(45+0j)
>>> complex(e)
(36.3+0j)
>>> c
(3+4j)
>>> c.real
3.0
>>> c.imag
4.0
>>> 
>>> str
<class 'str'>
>>> str(a)
'10'
>>> str(b)
'20.9'
>>> str(c)
'(3+4j)'
>>> eval(str(c))
(3+4j)
>>> 
>>> f = [3,4,6]
>>> int(f)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    int(f)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
>>> list(a)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
>>> list(b)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
>>> list(c)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
>>> list(d)
['4', '5']
>>> d
'45'
>>> list('abcdefghijklmnopqrstuvwxyz')
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
>>> ['a','b','c']
['a', 'b', 'c']
>>> list('abc')
['a', 'b', 'c']
>>> str(f)
'[3, 4, 6]'
>>> g = (8,4,9)
>>> str(g)
'(8, 4, 9)'
>>> list(g)
[8, 4, 9]
>>> tuple(f)
(3, 4, 6)
>>> tuple(d)
('4', '5')
>>> 
>>> h = {0:45,'a':[3,45]}
>>> str(h)
"{0: 45, 'a': [3, 45]}"
>>> list(h)
[0, 'a']
>>> tuple(h)
(0, 'a')
>>> 
>>> f
[3, 4, 6]
>>> dict(d)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    dict(d)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> dict(f)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    dict(f)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> g
(8, 4, 9)
>>> f1 = [4,5]
>>> dict(f1)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    dict(f1)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> f1 = [[4,5]]
>>> dict(f1)
{4: 5}
>>> f2 = [[4,5,6,7,8]]
>>> dict(f2)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    dict(f2)
ValueError: dictionary update sequence element #0 has length 5; 2 is required
>>> f2 = [[4,[5,6,7,8]]]
>>> dict(f2)
{4: [5, 6, 7, 8]}
>>> f2 = [[4,[5,6,7,8]],('one','NICE')]
>>> dict(f2)
{4: [5, 6, 7, 8], 'one': 'NICE'}
>>> 
>>> set(a)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
>>> set(f)
{3, 4, 6}
>>> set(h)
{0, 'a'}
>>> z
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    z
NameError: name 'z' is not defined
>>> z = 100
>>> z
100
>>> y
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    y
NameError: name 'y' is not defined
>>> 
>>> p = '''
y = a*10
print(y)
y += 3
print(y)
'''
>>> p
'\ny = a*10\nprint(y)\ny += 3\nprint(y)\n'
>>> print(p)

y = a*10
print(y)
y += 3
print(y)

>>> exec(p)
100
103
>>> y
103
>>> exec('abcd')
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    exec('abcd')
  File "<string>", line 1, in <module>
NameError: name 'abcd' is not defined
>>> abcd
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    abcd
NameError: name 'abcd' is not defined
>>> 