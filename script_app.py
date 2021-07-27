import tkinter as tk
app = tk.Tk(__name__)
app.title('My GUI')
app.geometry('300x200')

##tk.Label(app, text='Hi I am a Text').pack()
##tk.Label(app, text='This is one').pack()
##tk.Label(app, text='two',fg='red').pack()
##tk.Label(app, text='End', font=('Arial',25)).pack()

##tk.Label(app, text='Hi I am a Text').grid(row=0,column=0)
##tk.Label(app, text='This is one').grid(row=1,column=0)
##tk.Label(app, text='two',fg='red').grid(row=1,column=1)
##tk.Label(app, text='End', font=('Arial',25)).grid(row=3,column=3)

##tk.Label(app, text='Hi I am a Text').place(x=20,y=20)
##tk.Label(app, text='This is one').place(x=20,y=50)
##tk.Label(app, text='two',fg='red').place(x=100,y=50)
##tk.Label(app, text='End', font=('Arial',25)).place(x=150,y=160)

msg = tk.Variable(app)
msg.set('')

ent = tk.Variable(app)
ent.set('')

tk.Label(app, textvariable = msg, font=('Arial',15)).place(x=30,y=150)
tk.Entry(app, textvariable = ent, font=('Arial',15)).place(x=30, y=40)

def click():
    print('Clicked')
    content = ent.get()
    msg.set('You said: '+ content)

tk.Button(app, text='Click Me', command=click, font=('Arial',15)).place(x=30,y=100)


app.mainloop()
