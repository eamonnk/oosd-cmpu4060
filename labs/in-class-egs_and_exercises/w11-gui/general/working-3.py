from tkinter import *
from tkinter import ttk

# she added this as uses newer frames/widgets


def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass


root = Tk()
root.title("Feet to Meters")



# we create a frame widget, which will hold the contents of our user interface.
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)

# mainfram goes into position 0 0 in the grid...
root.rowconfigure(0, weight=1)
# zero just means no rows and no columns....
# after the frame is created grid places it directly inside out main app windows
# framne has all the default styling, so grey background etc
# so always a good idea to add a frame

# a tcl striong vcariable => if user writes into the feet
# feet is a special strinkg class....is a child of the mainframe...
feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=10, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
feet_entry.focus()
root.bind("<Return>", calculate)

l.label()


# mainloop has ot be at the end ....
# mainloop is an infinite loop so have to stop it...
root.mainloop()