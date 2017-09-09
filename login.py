from tkinter import *
import tkinter.messagebox
root=Tk()
d={}
def fibb(n):
 if n in d:
  return d[n]
 elif n<3:
  d[n]=1
  return d[n]
 else:
  d[n]=fibb(n-1)+fibb(n-2)
  return d[n]
def calc():
 s=entry.get()
 if s is "":
  tkinter.messagebox.showinfo("Exception","Field empty")
  return
 n=int(s)
 ans=fibb(n)
 tkinter.messagebox.showinfo("ans",ans)
button=Button(root,text="calculate",command=calc,bg="black",fg="red")
entry=Entry(root)
frame=Frame(root,width=300,height=100)
frame2=Frame(root,width=300,height=100)
frame.grid(row=0,column=1)
label=Label(root,text="Fibbonacci")
label.grid(row=1,sticky="W")
entry.grid(row=1,column=1)
button.grid(row=2,columnspan=2)
frame2.grid(row=3,column=1)
root.mainloop()
