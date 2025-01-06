# from tkinter import *
# from tkinter import ttk
# root = Tk()
# l =ttk.Label(root, text="Starting...")
# l.grid()
# l.bind('<Enter>', lambda e: l.configure(text='Moved mouse inside'))
# l.bind('<Leave>', lambda e: l.configure(text='Moved mouse outside'))
# l.bind('<ButtonPress-1>', lambda e: l.configure(text='Clicked left mouse button'))
# l.bind('<3>', lambda e: l.configure(text='Clicked right mouse button'))
# l.bind('<Double-1>', lambda e: l.configure(text='Double clicked'))
# l.bind('<B3-Motion>', lambda e: l.configure(text='right button drag to %d,%d' % (e.x, e.y)))
# root.mainloop()

import csv
import os
from pathlib import Path



# https://docs.python.org/3/library/os.path.html ++ https://sqlpey.com/python/top-10-methods-to-retrieve-full-path/
py_file_location=os.path.dirname(os.path.realpath(__file__))
csv_file_name="match_analysis.csv"
csv_file_name_and_path=os.path.join(py_file_location, csv_file_name)

csv_file_headers=[
    'date', 'month', 'year', 'ko time', 'home_team', 'away_team',
    'shots_on_target', 'shots_off_target', 'free_kicks_for', 
    'free_kicks_against', 'goals_for', 'goals_against'
]


def csv_file_create(csv_file_name):
    if not os.path.isfile(csv_file_name_and_path):
        with open(csv_file_name_and_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(csv_file_headers)
        print(f" csv file '{csv_file_name}' created with headers")        
    
    else:
        print(f" csv file '{csv_file_name}' already exists")
        dir=os.path.dirname
        print(dir)
    
csv_file_create(csv_file_name)