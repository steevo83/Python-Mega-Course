from tkinter import *

window = Tk()

def convert():
    t1.delete("1.0",END)
    t1.insert(END, f'{float(e1Value.get())*1000}g')
    t2.delete("1.0",END)
    t2.insert(END, f'{float(e1Value.get())*2.20462}lbs')
    t3.delete("1.0",END)
    t3.insert(END, f'{float(e1Value.get())*35.274}ozs')


l1 = Label(window, text="Kg")
l1.grid(row=0, column=0)

e1Value=StringVar()
e1 = Entry(window, textvariable=e1Value)
e1.grid(row=0, column=1)

b1 = Button(window, text="Convert", command=convert)
b1.grid(row=0, column=2)

t1 = Text(window, height=1, width=20)
t1.grid(row=1, column=0)

t2  = Text(window, height=1, width=20)
t2.grid(row=1, column=1)

t3 = Text(window, height=1, width=20)
t3.grid(row=1, column=2)

window.mainloop()