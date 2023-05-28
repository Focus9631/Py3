from tkinter import*

calc = Tk()
calc.title = 'Калькулятор'

a = Entry(width=16)
b = Entry(width=16)
c = Button(text="+")
b1 = Button(text="-")
b2 = Button(text="*")
b3 = Button(text="/")
L = Label (bg="black",fg="white",width=16)

def plus(event):
    s1= int(a.get())
    s2= int(b.get())
    s3= str(s1+s2)
    L['text']=s3

c.bind('<Button-1>', plus)

def minus(event):
    s1= int(a.get())
    s2= int(b.get())
    s3= str(s1-s2)
    L['text']=s3

b1.bind('<Button-1>', minus)

def multiply(event):
    s1= int(a.get())
    s2= int(b.get())
    s3= str(s1*s2)
    L['text']=s3

b2.bind('<Button-1>', multiply)
def take(event):
    s1= int(a.get())
    s2= int(b.get())
    s3= str(s1/s2)
    L['text']=s3

b3.bind('<Button-1>', take)

a.pack()
b.pack()
c.pack()
b1.pack()
b2.pack()
b3.pack()
L.pack()
calc.mainloop()
