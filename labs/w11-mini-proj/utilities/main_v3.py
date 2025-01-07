from match_analysis_v5 import MatchAnalysis
from planet_travel_time_v3 import PlanetTravelTime
from gravity_v1 import Gravity
import tkinter as tk # used for tk works
from tkinter import ttk # some ttk widgets used
from tkinter import StringVar
import os # used for filer and path work
import csv # used for csv file work
from pathlib import Path


def ma_utility_button_click():
    ma_utility=MatchAnalysis(master=root)
    ma_utility.start_match_analysis_app()

# create main app root window
root = tk.Tk()
root.title("Mini project - 3 applications - Jan 2025")

# create main app windows frame and place it using grid()
app_frame = tk.Frame(root, borderwidth=2, relief="groove", padx=5, pady=10)
app_frame.grid(row=0, column=0, padx=10, pady=10, sticky=('N', 'W', 'E', 'S'))

# Create header text and description text for frame and place them using grid()
app_frame_header = ttk.Label(app_frame, text="Mini Project - 3 Utilities", font=("Helvetica", 10, "bold"))
app_frame_header.grid(row=0, column=0, columnspan=2)
app_frame_desc = ttk.Label(app_frame, text="This application contains 3 separate utilities. Click the utility button to launch the specific utility.", font=("Helvetica", 8, "normal"))
app_frame_desc.grid(row=1, column=0, columnspan=3, padx=1, pady=1, sticky="w, n")

# craete utility and Help buttons
match_analysis_button=tk.Button(app_frame, text="Match Analysis", padx=5, pady=5, underline=True, background='white', command=ma_utility_button_click)
match_analysis_button.grid(row=2, column=1, padx=10, pady=5, sticky='e')


# root = tk.Tk()
# app1=MatchAnalysis()
# app1.start_match_analysis_app()

# # root = tk.Tk()
# app2=PlanetTravelTime()
# app2.start_planet_travel_time_app()

# # root = tk.Tk()
# app3=Gravity()
# app3.start_gravity_app()

root.mainloop()