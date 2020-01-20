from tkinter import *

# Tk() is a function of tkinter
window = Tk()

def kmToMiles():
    # print(e1Value.get())
    miles = f'{float(e1Value.get())*1.6}\n'
    t1.insert(END, miles)

b1=Button(window, text="Execute", command=kmToMiles)
b1.grid(row=0, column=0)

e1Value=StringVar()
e1=Entry(window, textvariable=e1Value)
e1.grid(row=0, column=1)

t1=Text(window, height=10, width=20)
t1.grid(row=0, column=2)


# Needed to close program
window.mainloop()