# import tkinter as tk


# def on_click():
#     print("Button clicked!")

# root = tk.Tk()
# button = tk.Button(root, text="Click Me", command=on_click)
# button.pack()
# root.mainloop()

import tkinter as tk
from tkinter import ttk

# Create main window
root = tk.Tk()
root.title("Dropdown List Example")
root.geometry("600x200")

# Dropdown values
options_1 = ["Option 1", "Option 2", "Option 3", "Option 4"]
options_2 = ["mercury", "venus", "earth", "mars"]

# Create Combobox
selected_option_1 = tk.StringVar()  # To store the selected value
dropdown_1 = ttk.Combobox(root, textvariable=selected_option_1, values=options_1)
selected_option_2 = tk.StringVar()  # To store the selected value
dropdown_2 = ttk.Combobox(root, textvariable=selected_option_2, values=options_2)

# Set default value
dropdown_1.set("Select an option 1")
dropdown_2.set("Select an option 2")

# Place the Combobox
dropdown_1.pack(pady=20)

dropdown_2.pack(pady=200)

# Function to get selected value
def show_selection_1():
    selection = selected_option_1.get()
    label.config(text=f"Selected: {selection_1}")

def show_selection_2():
    selection = selected_option_2.get()
    label.config(text=f"Selected: {selection_2}")

# Button to trigger action
button = ttk.Button(root, text="Submit", command=show_selection_1)
button.pack(pady=10)

button = ttk.Button(root, text="Submit", command=show_selection_2)
button.pack(pady=10)


# Label to display the selection
label = ttk.Label(root, text="")
label.pack()

# Run the application
root.mainloop()
