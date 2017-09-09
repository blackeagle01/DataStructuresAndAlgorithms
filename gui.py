from tkinter import *
from tkinter import ttk
root=Tk()
root.resizable(1,0)
e=Entry(root,width=10)
def show():
 a=str(new.get())
 print("hello "+e.get()+a) 
def fun():
 a=rad.get()
 if a is 1:
  root.configure(background="Red")
 else:
  root.configure(background="Blue")
b=Button(root,text="send names",command=show).grid(row=0,column=2)
new=IntVar()
ttk.Combobox(root,width=12,values=tuple(range(10)),textvariable=new).grid(row=0,column=1)
rad=IntVar()
Radiobutton(root,text="red",command=fun,value=1,variable=rad).grid(row=1,column=0)
Radiobutton(root,text="blue",command=fun,value=2,variable=rad).grid(row=1,column=1)
e.grid(row=0,column=0)
e.focus()
root.mainloop()
