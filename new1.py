from tkinter import *
from tkinter import ttk
root=Tk()
mainframe=ttk.LabelFrame(root)
root.title("MachineLearn")
mainframe.grid(padx=350,pady=200)
child=ttk.Labelframe(mainframe,text="Select Printer")
child.grid(padx=35,pady=10,columnspan=2)
child1=ttk.Labelframe(mainframe,text="Page range")
child1.grid(row=1,padx=15,pady=10)
child2=ttk.Labelframe(mainframe,text="Page range")
child2.grid(row=1,column=1,padx=20,pady=10)
root.mainloop()
