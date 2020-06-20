from tkinter import *

# math function


def add(a, b):
    return a+b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def mod(a, b):
    return a % b


def lcm(a, b):
    L = a if a > b else b
    while L <= a*b:
        if L % a == 0 and L % b == 0:
            return L
        L += 1


def hcf(a, b):
    H = a if a < b else b
    while H >= 1:
        if a % H == 0 and b % H == 0:
            return H
        H -= 1


def extractfromtext(text):
    l = []
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return l


def calculate():
    text = textin.get()
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                l = extractfromtext(text)
                r = operations[word.upper()](l[0], l[1])
                list.delete(0, END)
                list.insert(END, r)
            except:
                list.delete(0, END)
                list.insert(END, 'something went wrong please enter again')
            finally:
                break
        elif word.upper() not in operations.keys():
            list.delete(0, END)
            list.insert(END, 'something went wrong please enter again')


operations = {'ADD': add, 'ADDITION': add, 'SUM': add, 'PLUS': add, '+': add, 'SUB': sub, 'SUBTRACT': sub, 'MINUS': sub, 'DIFFERENCE': sub, '-': sub, 'HCF': hcf,
              'LCM': lcm, 'PRODUCT': mul, '*': mul, "MULTIPLY": mul, 'MULTIPLICATION': mul, 'DIV': div, '/': div, 'DIVISION': div, 'MOD': mod, '%': mod, 'REMAINDER': mod, 'MODULUS': mod}


win = Tk()
win.geometry('500x300')
win.title('Smart Calculator')
win.configure(bg='lightgreen')

l1 = Label(win, text='Smart Calculator', width=20, padx=3)
l1.place(x=150, y=10)
l2 = Label(win, text='creator AnimeshRy', width=20, padx=3)
l2.place(x=150, y=40)
l3 = Label(win, text="What's the equation ? ", width=20, padx=3)
l3.place(x=150, y=130)

textin = StringVar()
el = Entry(win, width=30, textvariable=textin)
el.place(x=140, y=160)
b1 = Button(win, text='Shall I start?', command=calculate)
b1.place(x=210, y=200)
list = Listbox(win, width=30, height=3)
list.place(x=140, y=230)
win.mainloop()
