Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> __annotations__
{}
>>> __build_class__
<built-in function __build_class__>
>>> __build_class__()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    __build_class__()
TypeError: __build_class__: not enough arguments
>>> __builtins__
<module 'builtins' (built-in)>
>>> __debug__
True
>>> __doc__
>>> __name__
'__main__'
>>> 
==== RESTART: C:/Users/hp/Desktop/UFT/15072021ML01/day10/script.py ====
Class bann gayi
>>> 
==== RESTART: C:/Users/hp/Desktop/UFT/15072021ML01/day10/script.py ====
Class bann gayi
>>> x = Abc()
>>> x
<__main__.Abc object at 0x0000021067D34C10>
>>> x.a
10
>>> 
>>> x.b
20
>>> Abc.a
10
>>> Abc.b
20
>>> y = Abc()
>>> type(y)
<class '__main__.Abc'>
>>> y.a
10
>>> x.a
10
>>> x.a=15
>>> x.a
15
>>> y.a
10
>>> Abc.b
20
>>> Abc.b=200
>>> x.b
200
>>> y.b
200
>>> Abc.b
200
>>> 
==== RESTART: C:/Users/hp/Desktop/UFT/15072021ML01/day10/script.py ====
Class bann gayi
>>> x = Abc()
>>> x.show()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    x.show()
TypeError: show() takes 0 positional arguments but 1 was given
>>> 
==== RESTART: C:/Users/hp/Desktop/UFT/15072021ML01/day10/script.py ====
Class bann gayi
>>> x = Abc()
>>> x.show()
Hum bhi aa gaye
10
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    x.show()
  File "C:/Users/hp/Desktop/UFT/15072021ML01/day10/script.py", line 11, in show
    print(b)
NameError: name 'b' is not defined
>>> 
==== RESTART: C:/Users/hp/Desktop/UFT/15072021ML01/day10/script.py ====
Class bann gayi
>>> x = Abc()
>>> x.show()
Hum bhi aa gaye
10
20
>>> 
==== RESTART: C:/Users/hp/Desktop/UFT/15072021ML01/day10/script.py ====
Class bann gayi
>>> x = Abc()
>>> x.show()
Hum bhi aa gaye
10
20
>>> y = Abc()
>>> z=Abc().show()
Hum bhi aa gaye
10
20
>>> del y
>>> y = Abc()
>>> y = 10
>>> print(y)
10
>>> print(x)
<__main__.Abc object at 0x000001B408924C70>
>>> x
<__main__.Abc object at 0x000001B408924C70>
>>> str(x)
'<__main__.Abc object at 0x000001B408924C70>'
>>> x()
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    x()
TypeError: 'Abc' object is not callable
>>> 
==== RESTART: C:/Users/hp/Desktop/UFT/15072021ML01/day10/script.py ====
Class bann gayi
>>> x  =Abc()
Constructor
>>> 
==== RESTART: C:/Users/hp/Desktop/UFT/15072021ML01/day10/script.py ====
Class bann gayi
>>> x =Abc()
Destructor
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    x =Abc()
TypeError: __init__() missing 1 required positional argument: 'm'
>>> x =Abc()
Destructor
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    x =Abc()
TypeError: __init__() missing 1 required positional argument: 'm'
>>> x =Abc(56)
Constructor 56 aaya hai
>>> del x
Destructor
>>> x =Abc(56)
Constructor 56 aaya hai
>>> x
good
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    x
TypeError: __repr__ returned non-string (type NoneType)
>>> 
==== RESTART: C:/Users/hp/Desktop/UFT/15072021ML01/day10/script.py ====
Class bann gayi
>>> x =Abc(56)
Constructor 56 aaya hai
>>> x
good
>>> print(x)
nice
>>> str(x)
'nice'
>>> x()
Arey wah.. ye to call ho gaya
>>> 
==== RESTART: C:/Users/hp/Desktop/UFT/15072021ML01/day10/script.py ====
Class bann gayi
>>> p = Pqr()
Destructor
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    p = Pqr()
TypeError: __init__() missing 1 required positional argument: 'm'
>>> p = Pqr(60)
Constructor 60 aaya hai
>>> p.new()
i am new
>>> p.show()
Hum bhi aa gaye
10
20
>>> 