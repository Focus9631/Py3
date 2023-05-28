from tkinter import*
 
Save = Tk()
Save.title ('OpenAndSAve')

e = Entry(width=20, justify=CENTER)
b1=Button(width=10, height=1, text='Open')
b2=Button(width=10, height=1, text='Save')
text = Text(width=30, height=10)
scroll = Scrollbar(command=text.yview)
scroll.pack(side=RIGHT, fill=Y)
text.config(yscrollcommand=scroll.set)
text.pack(side=BOTTOM)
e.pack(side=LEFT)
def openfile():
    f=open(e.get(),'r')
    a=f.read()
    text.insert(1.0,a)
    f.close()
b1.config(command=openfile)
def savefile():
    f2=open(e.get(),'w')
    a=text.get(1.0,END)
    f2.write(a)
    f2.close()
b2.config(command=savefile)
b1.pack(side=LEFT)
b2.pack(side=LEFT)
