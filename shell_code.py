Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = [34,'45','Hello',56,3.4,[9,4,44,'hi']]
>>> a[2]
'Hello'
>>> aa = a[2]
>>> aa[0]
'H'
>>> a[2][0]
'H'
>>> a[-1]
[9, 4, 44, 'hi']
>>> a[-1][-1]
'hi'
>>> a[-1][-1][-1]
'i'
>>> a[-1][-1][1]
'i'
>>> [5,6,8] + [5,'go']
[5, 6, 8, 5, 'go']
>>> a += ['good']
>>> a
[34, '45', 'Hello', 56, 3.4, [9, 4, 44, 'hi'], 'good']
>>> a += ['go','bye',45]
>>> a
[34, '45', 'Hello', 56, 3.4, [9, 4, 44, 'hi'], 'good', 'go', 'bye', 45]
>>> a = a[:2] + [66] + a[2:]
>>> a
[34, '45', 66, 'Hello', 56, 3.4, [9, 4, 44, 'hi'], 'good', 'go', 'bye', 45]
>>> a += 'nice'
>>> a
[34, '45', 66, 'Hello', 56, 3.4, [9, 4, 44, 'hi'], 'good', 'go', 'bye', 45, 'n', 'i', 'c', 'e']
>>> a += (9,4,'one')
>>> a
[34, '45', 66, 'Hello', 56, 3.4, [9, 4, 44, 'hi'], 'good', 'go', 'bye', 45, 'n', 'i', 'c', 'e', 9, 4, 'one']
>>> 
>>> a[0] = 340
>>> a
[340, '45', 66, 'Hello', 56, 3.4, [9, 4, 44, 'hi'], 'good', 'go', 'bye', 45, 'n', 'i', 'c', 'e', 9, 4, 'one']
>>> a[0] = '340'
>>> a
['340', '45', 66, 'Hello', 56, 3.4, [9, 4, 44, 'hi'], 'good', 'go', 'bye', 45, 'n', 'i', 'c', 'e', 9, 4, 'one']
>>> del a[6:10]
>>> a
['340', '45', 66, 'Hello', 56, 3.4, 45, 'n', 'i', 'c', 'e', 9, 4, 'one']
>>> 
>>> s = 'hi it is something'
>>> s[0] = 'K'
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    s[0] = 'K'
TypeError: 'str' object does not support item assignment
>>> del s[0]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    del s[0]
TypeError: 'str' object doesn't support item deletion
>>> 
>>> t = (10,20,30,'40',50.0)
>>> type(t)
<class 'tuple'>
>>> type(a)
<class 'list'>
>>> len(a)
14
>>> len(t)
5
>>> t[0]
10
>>> t[-2]
'40'
>>> t[-2][-1]
'0'
>>> t1 = 10,20,'n9c'
>>> t1
(10, 20, 'n9c')
>>> type(t1)
<class 'tuple'>
>>> t1 += (600)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    t1 += (600)
TypeError: can only concatenate tuple (not "int") to tuple
>>> t1 += (600,)
>>> t1
(10, 20, 'n9c', 600)
>>> t1 += 'good'
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    t1 += 'good'
TypeError: can only concatenate tuple (not "str") to tuple
>>> t1 += [7,6,54]
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    t1 += [7,6,54]
TypeError: can only concatenate tuple (not "list") to tuple
>>> t1[0] = 44
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    t1[0] = 44
TypeError: 'tuple' object does not support item assignment
>>> del t1[0]
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    del t1[0]
TypeError: 'tuple' object doesn't support item deletion
>>> 
>>> 
>>> #dictionary = {key:value}
>>> 
>>> cars = {'brand':['Tata','Maruti','Hyundai'], 'model':['Indica','800','Santro'],'price':[150000,60000,100000]}
>>> type(cars)
<class 'dict'>
>>> print(cars)
{'brand': ['Tata', 'Maruti', 'Hyundai'], 'model': ['Indica', '800', 'Santro'], 'price': [150000, 60000, 100000]}
>>> len(cars)
3
>>> d = {1:3.4,'0':34,9.3:[7,8]}
>>> len(d)
3
>>> d1 = {}
>>> len(d1)
0
>>> cars['brand']
['Tata', 'Maruti', 'Hyundai']
>>> cars[0]
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    cars[0]
KeyError: 0
>>> cars['price']
[150000, 60000, 100000]
>>> cars['price'][-1]
100000
>>> cars['year'] = (2008,2006,2005)
>>> cars
{'brand': ['Tata', 'Maruti', 'Hyundai'], 'model': ['Indica', '800', 'Santro'], 'price': [150000, 60000, 100000], 'year': (2008, 2006, 2005)}
>>> cars['model'] = ['IndicaV2', '800', 'Santro']
>>> cars['model'][-1] = 'Santro Xing'
>>> cars
{'brand': ['Tata', 'Maruti', 'Hyundai'], 'model': ['IndicaV2', '800', 'Santro Xing'], 'price': [150000, 60000, 100000], 'year': (2008, 2006, 2005)}
>>> cars[5]:66
>>> cars
{'brand': ['Tata', 'Maruti', 'Hyundai'], 'model': ['IndicaV2', '800', 'Santro Xing'], 'price': [150000, 60000, 100000], 'year': (2008, 2006, 2005)}
>>> cars[5]=66
>>> cars
{'brand': ['Tata', 'Maruti', 'Hyundai'], 'model': ['IndicaV2', '800', 'Santro Xing'], 'price': [150000, 60000, 100000], 'year': (2008, 2006, 2005), 5: 66}
>>> cars['new']=66
>>> cars
{'brand': ['Tata', 'Maruti', 'Hyundai'], 'model': ['IndicaV2', '800', 'Santro Xing'], 'price': [150000, 60000, 100000], 'year': (2008, 2006, 2005), 5: 66, 'new': 66}
>>> del cars[5]
>>> del cars['new']
>>> cars
{'brand': ['Tata', 'Maruti', 'Hyundai'], 'model': ['IndicaV2', '800', 'Santro Xing'], 'price': [150000, 60000, 100000], 'year': (2008, 2006, 2005)}
>>> 
>>> p = {8,5,6,'hi',6,8,5,3,8,5}
>>> type(p)
<class 'set'>
>>> len(p)
5
>>> p
{3, 'hi', 5, 6, 8}
>>> p[0]
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    p[0]
TypeError: 'set' object is not subscriptable
>>> 
>>> 
>>> ### Built-in Functions for Data Classes
>>> ########################################
>>> s
'hi it is something'
>>> s.capitalize()
'Hi it is something'
>>> s.upper()
'HI IT IS SOMETHING'
>>> s
'hi it is something'
>>> s1 = s.upper()
>>> s1
'HI IT IS SOMETHING'
>>> s.count('i')
4
>>> s.count('it')
1
>>> s.count('axe')
0
>>> s.find('is')
6
>>> # lower, upper, find, count, format, join, split, strip, ::: isalpha, isnumeric, islower
>>> s.split()
['hi', 'it', 'is', 'something']
>>> s.split('i')
['h', ' ', 't ', 's someth', 'ng']
>>> s2 = 'peeyush.sanam'
>>> '@'.join([s2, 'gmail.com'])
'peeyush.sanam@gmail.com'
>>> '-'.join(s.split())
'hi-it-is-something'
>>> s.replace(' ', '-')
'hi-it-is-something'
>>> 
>>> help(s.count)
Help on built-in function count:

count(...) method of builtins.str instance
    S.count(sub[, start[, end]]) -> int
    
    Return the number of non-overlapping occurrences of substring sub in
    string S[start:end].  Optional arguments start and end are
    interpreted as in slice notation.

>>> k = 'sssss'
>>> k.count('ss')
2
>>> ##############
>>> # LIST Functions
>>> ##################
>>> a
['340', '45', 66, 'Hello', 56, 3.4, 45, 'n', 'i', 'c', 'e', 9, 4, 'one']
>>> a.append(600)
>>> a
['340', '45', 66, 'Hello', 56, 3.4, 45, 'n', 'i', 'c', 'e', 9, 4, 'one', 600]
>>> a.append(600,700)
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    a.append(600,700)
TypeError: list.append() takes exactly one argument (2 given)
>>> a.extend(750,'hi')
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    a.extend(750,'hi')
TypeError: list.extend() takes exactly one argument (2 given)
>>> a.append([600,700])
>>> a
['340', '45', 66, 'Hello', 56, 3.4, 45, 'n', 'i', 'c', 'e', 9, 4, 'one', 600, [600, 700]]
>>> a.extend([750,'hi'])
>>> a
['340', '45', 66, 'Hello', 56, 3.4, 45, 'n', 'i', 'c', 'e', 9, 4, 'one', 600, [600, 700], 750, 'hi']
>>> a.index('z')
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    a.index('z')
ValueError: 'z' is not in list
>>> a.index(66)
2
>>> 'z' in a
False
>>> a.insert(4,'wow')
>>> a
['340', '45', 66, 'Hello', 'wow', 56, 3.4, 45, 'n', 'i', 'c', 'e', 9, 4, 'one', 600, [600, 700], 750, 'hi']
>>> a.pop()
'hi'
>>> a
['340', '45', 66, 'Hello', 'wow', 56, 3.4, 45, 'n', 'i', 'c', 'e', 9, 4, 'one', 600, [600, 700], 750]
>>> a.pop(4)
'wow'
>>> a
['340', '45', 66, 'Hello', 56, 3.4, 45, 'n', 'i', 'c', 'e', 9, 4, 'one', 600, [600, 700], 750]
>>> a.remove('45')
>>> a
['340', 66, 'Hello', 56, 3.4, 45, 'n', 'i', 'c', 'e', 9, 4, 'one', 600, [600, 700], 750]
>>> a[::-1]
[750, [600, 700], 600, 'one', 4, 9, 'e', 'c', 'i', 'n', 45, 3.4, 56, 'Hello', 66, '340']
>>> a.reverse()
>>> a
[750, [600, 700], 600, 'one', 4, 9, 'e', 'c', 'i', 'n', 45, 3.4, 56, 'Hello', 66, '340']
>>> a.sort()
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    a.sort()
TypeError: '<' not supported between instances of 'list' and 'int'
>>> y = [4,7,234,678,34,76]
>>> y.sort()
>>> y
[4, 7, 34, 76, 234, 678]
>>> 
>>> a
[750, [600, 700], 600, 'one', 4, 9, 'e', 'c', 'i', 'n', 45, 3.4, 56, 'Hello', 66, '340']
>>> a2 = a
>>> a2
[750, [600, 700], 600, 'one', 4, 9, 'e', 'c', 'i', 'n', 45, 3.4, 56, 'Hello', 66, '340']
>>> del a2[-10:]
>>> a2
[750, [600, 700], 600, 'one', 4, 9]
>>> a
[750, [600, 700], 600, 'one', 4, 9]
>>> id(a2)
2042020870912
>>> id(a)
2042020870912
>>> a3 = a.copy()
>>> a3
[750, [600, 700], 600, 'one', 4, 9]
>>> a
[750, [600, 700], 600, 'one', 4, 9]
>>> a3[0] = 7
>>> a3
[7, [600, 700], 600, 'one', 4, 9]
>>> a
[750, [600, 700], 600, 'one', 4, 9]
>>> 
>>> ############
>>> # Tuple
>>> ############
>>> t
(10, 20, 30, '40', 50.0)
>>> t.count(10)
1
>>> t.index(10)
0
>>> 
>>> ############
>>> # Dictionary
>>> #############
>>> cars
{'brand': ['Tata', 'Maruti', 'Hyundai'], 'model': ['IndicaV2', '800', 'Santro Xing'], 'price': [150000, 60000, 100000], 'year': (2008, 2006, 2005)}
>>> cars['brand']
['Tata', 'Maruti', 'Hyundai']
>>> cars['fuel_type']
Traceback (most recent call last):
  File "<pyshell#169>", line 1, in <module>
    cars['fuel_type']
KeyError: 'fuel_type'
>>> cars.get('fuel_type')
>>> cars.get('price')
[150000, 60000, 100000]
>>> cars.keys()
dict_keys(['brand', 'model', 'price', 'year'])
>>> cars.values()
dict_values([['Tata', 'Maruti', 'Hyundai'], ['IndicaV2', '800', 'Santro Xing'], [150000, 60000, 100000], (2008, 2006, 2005)])
>>> cars[55]=6000
>>> cars
{'brand': ['Tata', 'Maruti', 'Hyundai'], 'model': ['IndicaV2', '800', 'Santro Xing'], 'price': [150000, 60000, 100000], 'year': (2008, 2006, 2005), 55: 6000}
>>> cars.pop(55)
6000
>>> cars
{'brand': ['Tata', 'Maruti', 'Hyundai'], 'model': ['IndicaV2', '800', 'Santro Xing'], 'price': [150000, 60000, 100000], 'year': (2008, 2006, 2005)}
>>> cars.items()
dict_items([('brand', ['Tata', 'Maruti', 'Hyundai']), ('model', ['IndicaV2', '800', 'Santro Xing']), ('price', [150000, 60000, 100000]), ('year', (2008, 2006, 2005))])
>>> 
>>> ###########
>>> # Set
>>> ###########
>>> 
>>> ########################
>>> # Typecasting
>>> ########################
>>> 