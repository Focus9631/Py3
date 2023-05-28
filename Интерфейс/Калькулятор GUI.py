from tkinter import *
 
root = Tk()
root.title("Калькулятор")
root.geometry("260x180") 
c = Entry(width=20)
a = Entry(width=20)
b = Button(text="+",width=16)
s = Button(text="-",width=16)
e = Button(text="*",width=16)
f = Button(text="/",width=16)
l = Label(bg='black', fg='white', width=20)
 

 
c.pack()
a.pack()
b.pack()
s.pack()
e.pack()
f.pack()
l.pack()
root.mainloop()
