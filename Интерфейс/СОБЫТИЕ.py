from tkinter import *
root = Tk()
root.minsize(width = 200, height=200)

def focusin(event):
        t['bg']='lightgrey'

def focusout(event):
        t['bg']='#ffffff'


def change(event):
    x=int(e1.get())
    y=int(e2.get())
    t['width']=x
    t['height']=y

e1 = Entry(width=3)
e2 = Entry(width=3)
b1 = Button(text="Изменить",width=10, height=1)
e1.pack()
e2.pack()
t = Text(width=5, height=3)
b1.bind('<Return>',change)
b1.bind('<Button-1>',change)
b1.pack()
t.focus_set()
t.bind('<FocusIn>',focusin)
t.bind('<FocusOut>',focusout)
t.pack()


root.mainloop()
