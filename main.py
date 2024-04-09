from tkinter import *
from tkinter import ttk

def call():
    e2.delete(0,END)
    n=eval(e1.get())
    s=[str(i) for i in range(1,n+1) if n%i==0]
    s=' '.join(s)
    e2.insert(0,s)

root=Tk()
l1=Label(text='Enter first N :')
l2=Label(text='the Double is  :')
e1=Entry()
e2=Entry()
b=Button(text='    Validate    ',command=call)
com = ttk.Combobox(root,state='readonly')

l1.grid(row=0,column=0,columnspan=2)
l2.grid(row=1,column=0,columnspan=2)
e1.grid(row=0,column=2)
e2.grid(row=1,column=2)
b.grid(row=3,column=2)


mainloop()