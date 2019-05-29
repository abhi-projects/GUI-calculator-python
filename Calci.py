from tkinter import *
fields = ('1', '2', '3', '+', '4', '5', '6', '-', '7', '8', '9', '*', '.', '0', '=', '/', 'POW', 'FLOOR', 'DEL', 'CLS')


def check(e):
    if e.get() == '0' or e.get() == 'ERROR':
        e.delete(0,END)


def evaluate(x, e):
    if x == 'POW':
        e.insert(END, '**')
    elif x == 'FLOOR':
        e.insert(END, '//')
    elif x == 'DEL':
        check(e)
        e.delete(len(e.get())-1, END)
        if e.get() == '':
            e.insert(0, '0')
    elif x == 'CLS':
        e.delete(0, END)
        e.insert(0, '0')
    elif x == '=':
        try:
            result = eval(e.get(), {'__builtins__': None}, {})
            e.delete(0, END)
            e.insert(0, str(result))
        except:
            e.delete(0, END)
            e.insert(0, 'ERROR')
    else:
        check(e)
        e.insert(END, x)


def make_structure():
    f1 = Frame(root)
    f1.pack(side=TOP, padx=5, pady=10)
    e = Entry(f1, width=70, font=('calibri', 14))
    e.insert(0, '0')
    e.pack(fill=X)
    j = 0
    for cnt in range(5):
        f = Frame(root)
        f.pack(side=TOP)
        for i in range(4):
            b = Button(f, text=fields[j], font=('Verdana', 16, 'bold'), width=4, command=lambda st=fields[j]: evaluate(st, e))
            b.pack(side=LEFT, padx=5, pady=5)
            j += 1


if __name__ == '__main__':
    root = Tk()
    root.geometry('400x300')
    root.wm_minsize(width=400, height=300)
    root.wm_maxsize(width=400, height=300)
    root.title('CALCI')
    make_structure()
    root.mainloop()

