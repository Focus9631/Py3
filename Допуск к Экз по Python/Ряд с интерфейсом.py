from tkinter import *

root = Tk()
root.title("Ряд")
root.geometry("530x445")


Label(text="i").grid(row=0, column=0, sticky=W, pady=5, padx=10)
Label(text="An").grid(row=0, column=0, sticky=W, pady=10, padx=130)
Label(text="Sum").grid(row=0, column=0, sticky=W, pady=10, padx=310)
q = ['']
text = Text(root, width=60, height=20)
scroll = Scrollbar(command=text.yview)


def mydef():
    n = 2
    eps = 5e-10
    an_1 = -1
    an = 0.25
    summa = -0.75
    while abs(an - an_1) > eps:
        an_1 = an
        an = 1 / ((3 * n - 2) * (3 * n + 1))
        summa += an
        q = f" {n} \t {an} \t    {an_1}"
        text.insert(INSERT, q+'\n')
        n = n + 1


btn = Button(root, text="Start", command=mydef)
btn.grid(row=2, column=0, sticky=W, pady=10, padx=230)
text.grid(row=1, column=0, sticky=W, pady=20, padx=10)
scroll.grid(row=1, column=0, sticky=W+S+N, padx=500)
root.mainloop()
