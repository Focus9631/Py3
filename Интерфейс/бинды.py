from tkinter import *
root = Tk()
 
def tp(event):
    x=e1.get()
    x=x.split()
    for i in x:
        lbox.insert(END,i)

def copy(event):
    select = list(lbox.curselection())
    x=e1.get()
    x=x.split()
    for i in select:
        t.insert(END,x[i])
 
e1 = Entry(width=50)
lbox = Listbox(selectmode=EXTENDED)
t = Text()
 
e1.bind('<Return>', tp)
lbox.bind('<Double-Button-1>',copy)

e1.pack()
lbox.pack()
t.pack()
 
root.mainloop()
