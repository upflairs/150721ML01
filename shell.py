Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy
>>> import numpy as np
>>> k = np.array([])
>>> k
array([], dtype=float64)
>>> type(k)
<class 'numpy.ndarray'>
>>> print(k)
[]
>>> len(k)
0
>>> k.shape
(0,)
>>> k.size
0
>>> a = np.array([5,6,8,3,8])
>>> a
array([5, 6, 8, 3, 8])
>>> print(a)
[5 6 8 3 8]
>>> type(a)
<class 'numpy.ndarray'>
>>> a.dtype
dtype('int32')
>>> a.shape
(5,)
>>> a.size
5
>>> len(a)
5
>>> b = np.array([[4,5],[8,7],[9,3]])
>>> b
array([[4, 5],
       [8, 7],
       [9, 3]])
>>> print(b)
[[4 5]
 [8 7]
 [9 3]]
>>> b.shape
(3, 2)
>>> b.size
6
>>> len(b)
3
>>> c = np.array(['hi','wow','])
	      
SyntaxError: EOL while scanning string literal
>>> c = np.array(['hi','wow','nice'])
>>> c
array(['hi', 'wow', 'nice'], dtype='<U4')
>>> c.dtype
dtype('<U4')
>>> d = np.array([4,'go'])
>>> d
array(['4', 'go'], dtype='<U11')
>>> e = np.array([[5,6],'good'])

Warning (from warnings module):
  File "<pyshell#29>", line 1
VisibleDeprecationWarning: Creating an ndarray from ragged nested sequences (which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes) is deprecated. If you meant to do this, you must specify 'dtype=object' when creating the ndarray.
>>> 
>>> np.arange(3,10,1)
array([3, 4, 5, 6, 7, 8, 9])
>>> np.arange(100,1,-10)
array([100,  90,  80,  70,  60,  50,  40,  30,  20,  10])
>>> np.linspace(3,10,20)
array([ 3.        ,  3.36842105,  3.73684211,  4.10526316,  4.47368421,
        4.84210526,  5.21052632,  5.57894737,  5.94736842,  6.31578947,
        6.68421053,  7.05263158,  7.42105263,  7.78947368,  8.15789474,
        8.52631579,  8.89473684,  9.26315789,  9.63157895, 10.        ])
>>> np.arange(3.5,10.3,1.37)
array([3.5 , 4.87, 6.24, 7.61, 8.98])
>>> list(range(3.5,10.3,1.37))
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    list(range(3.5,10.3,1.37))
TypeError: 'float' object cannot be interpreted as an integer
>>> np.zeros(4,5)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    np.zeros(4,5)
TypeError: Cannot interpret '5' as a data type
>>> np.zeros((4,5))
array([[0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.]])
>>> np.ones((3,4))
array([[1., 1., 1., 1.],
       [1., 1., 1., 1.],
       [1., 1., 1., 1.]])
>>> np.eye(4)
array([[1., 0., 0., 0.],
       [0., 1., 0., 0.],
       [0., 0., 1., 0.],
       [0., 0., 0., 1.]])
>>> p = np.array([[3,8,9,11],[17,16,18,21],[14,2,7,8]])
>>> p
array([[ 3,  8,  9, 11],
       [17, 16, 18, 21],
       [14,  2,  7,  8]])
>>> p[0,3]
11
>>> p[1,2]
18
>>> p[0][3]
11
>>> p[1][2]
18
>>> p[1]
array([17, 16, 18, 21])
>>> p[:][1]
array([17, 16, 18, 21])
>>> 
>>> p[:, 1]
array([ 8, 16,  2])
>>> p[1:,2:]
array([[18, 21],
       [ 7,  8]])
>>> p[:, 1:2]
array([[ 8],
       [16],
       [ 2]])
>>> q = np.array([[[3,13],[8,18],[9,19],[11,111]],[[12,112],[16,116],[18,118],[21,121]],[[14,114],[2,12],[7,17],[8,18]]])
>>> q.shape
(3, 4, 2)
>>> print(q)
[[[  3  13]
  [  8  18]
  [  9  19]
  [ 11 111]]

 [[ 12 112]
  [ 16 116]
  [ 18 118]
  [ 21 121]]

 [[ 14 114]
  [  2  12]
  [  7  17]
  [  8  18]]]
>>> q[0,0:2,0]
array([3, 8])
>>> q[2,2:,:]
array([[ 7, 17],
       [ 8, 18]])
>>> q[2:3,2:,:]
array([[[ 7, 17],
        [ 8, 18]]])
>>> 
>>> q[:2,2:,0:1]
array([[[ 9],
        [11]],

       [[18],
        [21]]])
>>> q[0:1,1:,1:]
array([[[ 18],
        [ 19],
        [111]]])
>>> q[1:,:1,:]
array([[[ 12, 112]],

       [[ 14, 114]]])
>>> q[0]
array([[  3,  13],
       [  8,  18],
       [  9,  19],
       [ 11, 111]])
>>> q[0,0,0]
3
>>> q[0,0,0] = 333
>>> q
array([[[333,  13],
        [  8,  18],
        [  9,  19],
        [ 11, 111]],

       [[ 12, 112],
        [ 16, 116],
        [ 18, 118],
        [ 21, 121]],

       [[ 14, 114],
        [  2,  12],
        [  7,  17],
        [  8,  18]]])
>>> 