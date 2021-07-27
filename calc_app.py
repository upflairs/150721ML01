import tkinter as tk
from math import sqrt
app = tk.Tk(__name__)
app.title('Calculator')
app.geometry('250x300')
evaluated = False
result = tk.Variable(app)
result.set('0')

tk.Label(app, textvariable=result,\
         width=20, bg='grey',height=2,
         font=('Arial',15),
         anchor='se',
         fg = 'white'
         ).place(x=15, y=5)

def show(v):
    global evaluated
    if result.get()=='0' or evaluated:
        evaluated = False
        result.set('')
    result.set(result.get()+v)
    
def calculate():
    global evaluated
    evaluated = True
    result.set(str(eval(result.get())))

def calc_sqrt():
    global evaluated
    evaluated = True
    result.set(str(sqrt(eval(result.get()))))

def backspace():
    if not (result.get()=='0' or evaluated):
        result.set(result.get()[:-1])

def clear():
    result.set('0')

tk.Button(app,text='AC',\
          command=clear,fg='white',bg='black',\
          font=('Arial',12),width=3,height=1
          ).place(x=15,y=80)
tk.Button(app,text='<-',\
          command=backspace,fg='white',bg='black',\
          font=('Arial',12),width=3,height=1
          ).place(x=80,y=80)
tk.Button(app,text='sqrt',\
          command=calc_sqrt,fg='white',bg='black',\
          font=('Arial',12),width=3,height=1
          ).place(x=145,y=80)
tk.Button(app,text='pwr',\
          command=lambda : show('**'),fg='white',bg='black',\
          font=('Arial',12),width=3,height=1
          ).place(x=205,y=80)
tk.Button(app,text='7',\
          command=lambda : show('7'),fg='white',bg='black',\
          font=('Arial',12),width=3,height=1
          ).place(x=15,y=120)
tk.Button(app,text='8',\
          command=lambda : show('8'),fg='white',bg='black',\
          font=('Arial',12),width=3,height=1
          ).place(x=80,y=120)
tk.Button(app,text='9',\
          command=lambda : show('9'),fg='white',bg='black',\
          font=('Arial',12),width=3,height=1
          ).place(x=145,y=120)
tk.Button(app,text='+',\
          command=lambda : show('+'),fg='white',bg='black',\
          font=('Arial',12),width=3,height=1
          ).place(x=205,y=120)
tk.Button(app,text='4',\
          command=lambda : show('4'),fg='white',bg='black',\
          font=('Arial',12),width=3,height=1
          ).place(x=15,y=160)
tk.Button(app,text='5',\
          command=lambda : show('5'),fg='white',bg='black',\
          font=('Arial',12),width=3,height=1
          ).place(x=80,y=160)
tk.Button(app,text='6',\
          command=lambda : show('6'),fg='white',bg='black',\
          font=('Arial',12),width=3,height=1
          ).place(x=145,y=160)
tk.Button(app,text='-',\
          command=lambda : show('-'),fg='white',bg='black',\
          font=('Arial',12),width=3,height=1
          ).place(x=205,y=160)
tk.Button(app,text='1',\
          command=lambda : show('1'),fg='white',bg='black',\
          font=('Arial',12),width=3,height=1
          ).place(x=15,y=200)
tk.Button(app,text='2',\
          command=lambda : show('2'),fg='white',bg='black',\
          font=('Arial',12),width=3,height=1
          ).place(x=80,y=200)
tk.Button(app,text='3',\
          command=lambda : show('3'),fg='white',bg='black',\
          font=('Arial',12),width=3,height=1
          ).place(x=145,y=200)
tk.Button(app,text='X',\
          command=lambda : show('*'),fg='white',bg='black',\
          font=('Arial',12),width=3,height=1
          ).place(x=205,y=200)
tk.Button(app,text='.',\
          command=lambda : show('.'),fg='white',bg='black',\
          font=('Arial',12),width=3,height=1
          ).place(x=15,y=240)
tk.Button(app,text='0',\
          command=lambda : show('0'),fg='white',bg='black',\
          font=('Arial',12),width=3,height=1
          ).place(x=80,y=240)
tk.Button(app,text='=',\
          command=calculate, fg='white',bg='black',\
          font=('Arial',12),width=3,height=1
          ).place(x=145,y=240)
tk.Button(app,text='/',\
          command=lambda:show('/'),fg='white',bg='black',\
          font=('Arial',12),width=3,height=1
          ).place(x=205,y=240)

app.mainloop()
