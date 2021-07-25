# In Python Functions can be:
# -> Assigned to a new object/variable
# -> Pass a function as an input
# -> Define Another function in a func
# -> Return a function from a function
# (Function Decorator)-> Flask Web App 

# Global Variable and Local Variable
# Annonymous Functions (Lambda Expression)
# Application Development using Tkinter

# (Generators) - Pandas

##########################################################
##def func():
##    print('Hi I am a function')
##
##k = func
##k()

##def onemore(x,a):
##    print(x(a))
##
##def ek(n):
##    return n**3
##
##onemore(ek, 30)

##def func2():
##    def func3():
##        print('wow')
##    print('Ok')
##    func3()
##
##func2()

##def func4():
##    def func5():
##        return 'nice'
##    return func5
##
##p = func4()
##print(p())


##ek1 = lambda n:n**3
##
##def onemore(x,a):
##    print(x(a))
##
##onemore(ek1, 2)


##def onemore(x,a):
##    print(x(a))
##
##onemore(lambda n:n**3, 2)

##a = [3,4,18,20,9,34,67,3,6,2,36,8,21,6,9]
##
##def myloop(f,c):
##    t = []
##    for i in c:        
##        t += [f(i)]
##    return t
##
##print(myloop(lambda n:n+10, a))
##print(myloop(lambda n:n//2, a))
##print(myloop(lambda n:n*2 if n%2 else n//2, a))

##a = 10
##def xyz():
##    a = 15
##    print(a)
##    
##print(a)
##xyz()
##print(a)

##a = 10
##def xyz():    
##    global a
##    print(a)
##    a = 15
##    print(a)
##    
##print(a)
##xyz()
##print(a)

##a = 10 
##def xyz():    
##    print(a) # Error
##    a = 15
##    print(a)
##    
##print(a)
##xyz()
##print(a)

##a = 10
##def xyz():    
##    print(a)
##    a1 = 15
##    print(a1)
##    
##print(a)
##xyz()
##print(a)

##a = 10
##y = 20
##def xyz():
##    x = 30
##    z = 0
##    def pqr():
##        print(x)
##        print(y)
##        nonlocal z
##        z = 50
##    pqr()
##    a = 15 + z
##    print(a)
##   
##    
##print(a, 'Direct')
##xyz()
##print(a, 'Direct')













