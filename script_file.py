##with open('data.csv','r') as f:
##    r3 = f.read()
##    f.close()
##print(r3)
##
##r = r3.split('\n')
##keys = r[0].split(',')
##values = ([i.split(',') for i in r[1:] if i])
##d = dict(zip(keys, zip(*values)))
##print(d)

# User Defined Functions
#-------------------------
# No Input / No Output
# Input / No Output
# No Input / Output
# Input / Output

# Multiple Input Args
# Multiple Output
# Keyword Arguments
# Optional Arguments (Default Values)
# Variable Number of Input Arguments
# Variable Keyword Arguments

# In Python Functions can be:
# -> Assigned to a new object/variable
# -> Pass a function as an input
# -> Define Another function in a func
# -> Return a function from a function


##def funcName():
##    pass

##def func1(): # no input, no o/p
##    print('ye mera function h python ka!!!!')
##
####func1()
####print('hahahahaha')
####func1()
##k = func1()

##def func2(x): # i/p, no o/p
##    print(x*4)
##
##func2(34)

##def func3(): # no i/p, o/p
##    return 'this is the output'
##
##k = func3()

##def func4(x): # i/p, o/p
##    return x*4
##
##k = func4('ha')
##print(k)

##def func5(x,y,z):
##    return (x+y)/z
##
##print(func5(3,4,6))


##def func6(x):
##    return x*2, x**3, x+4
##
##print(func6(3))
##m,n,p = func6(9)

##func5(x=10,z=30,y=4)


##def func7(x,y=0,z=1):
##    return (x+y)/z
##
##print(func7(3))

##def func8(*b):
##    print(b)
##
##func8()
##func8(7)
##func8(19,30)
##func8('hi','bye','go')
##a = [3,4,5,6,7]
##func8(a)
##func8(*a)

def func9(**b):
    print(b)

func9()
func9(name='Sanaya')
func9(plate=5, amount=30)

#(*args, **kwargs)












