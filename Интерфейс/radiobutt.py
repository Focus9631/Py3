from tkinter import *

def change():
    if var.get()==0:
        lab['text']='Artem'
    elif var.get()==1:
        lab['text']='Arina'
    elif var.get()==2:
        lab['text']='Alina'
root=Tk()
root.title('RadioButton')

var=IntVar()
b1= Radiobutton(text='Artem', variable=var, value=0, indicatoron=0, command=change)
b2= Radiobutton(text='Arina', variable=var, value=1, indicatoron=0, command=change)
b3= Radiobutton(text='Alina', variable=var, value=2, indicatoron=0, command=change)
lab=Label(width=20,height=10)
b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)
lab.pack(side=TOP)
root.mainloop()
