from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()

ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
frm2 = ttk.Frame(root, padding=100)
frm.grid()
ttk.Label(frm, text="Hello World 2!").grid(column=1, row=1)
ttk.Button(frm, text="Quit 2", command=root.destroy).grid(column=2, row=3)
root.mainloop()