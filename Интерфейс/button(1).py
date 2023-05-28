from tkinter import*
 
root = Tk()
root.title ('Кнопки радуги')

e = Entry(width=20, justify=CENTER)
e.pack()
L = Label(width=20,height=1)
L.pack()

b1 = Button(text="Красный", width=15, height=4) 
def change():
    e.insert(0,'#ff0000')
    L['text']='Красный'
    b1['bg'] = '#ff0000'

 
b1.config(command=change)
 
b1.pack()

b2 = Button(text="Оранжевый", width=15, height=4)
def change():
    e.delete(0,END)
    e.insert(0,'#ff7d00')
    L['text']='Оранжевый'
    b2['bg'] = '#ff7d00'

b2.config(command=change)
b2.pack()

b3 = Button(text="Желтый", width=15, height=4)
def change():
    e.delete(0,END)
    e.insert(0,'#ffff00')
    L['text']='Желтый'
    b3['bg'] = '#ffff00'
 
b3.config(command=change)
b3.pack()

b4 = Button(text="Зелёный", width=15, height=4)
def change():
    e.delete(0,END)
    e.insert(0,'#00ff00')
    L['text']='Зеленый'
    b4['bg'] = '#00ff00'
 
b4.config(command=change)
b4.pack()

b5 = Button(text="Голубой", width=15, height=4)
def change():
    e.delete(0,END)
    e.insert(0,'#007dff')
    L['text']='Голубой'
    b5['bg'] = '#007dff'

b5.config(command=change)
b5.pack()

b6 = Button(text="Синий", width=15, height=4)
def change():
    e.delete(0,END)
    e.insert(0,'#0000ff')
    L['text']='Синий'
    b6['bg'] = '#0000ff'
    
b6.config(command=change)
b6.pack()

b7 = Button(text="Фиолетовый", width=15, height=4)
def change():
    e.delete(0,END)
    e.insert(0,'#7d00ff')
    L['text']='Фиолетовый'
    b7['bg'] = '#7d00ff'

b7.config(command=change)
b7.pack()

root.mainloop()
