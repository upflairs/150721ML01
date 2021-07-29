# Object Oriented Programming
# -----------------------------
class Abc():
    print('Class bann gayi')
    a = 10
    b = 20

    def show(self):
        print('Hum bhi aa gaye')
        print(self.a)
        print(Abc.b)

    def __init__(self, m):
        print('Constructor', m, 'aaya hai')

    def __del__(self):
        print('Destructor')

    def __str__(self):        
        return 'nice'

    def __repr__(self):        
        return 'good'

    def __call__(self):
        print('Arey wah.. ye to call ho gaya')

class Pqr(Abc,):
    def new(self):
        print('i am new')
