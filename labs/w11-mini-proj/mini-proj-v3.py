import tkinter as tk
from tkinter import ttk
from tkinter import StringVar
import csv

# Create the main root window, this is the parent for each frame
root = tk.Tk()
root.title("Mini project - 3 applications - Jan 2025")



# Create 3 separate frames with borders, one for each of the 3 applications, so we can demarcate between them.
frame1_sports = tk.Frame(root, borderwidth=2, relief="groove", padx=5, pady=10)
frame2_planets = tk.Frame(root, borderwidth=2, relief="groove", padx=5, pady=10)
frame3_gravity = tk.Frame(root, borderwidth=2, relief="groove", padx=5, pady=10)


# Place the frames in the main window using grids with some padding between them and align west
frame1_sports.grid(row=0, column=0, padx=10, pady=10, sticky=('N', 'W', 'E', 'S'))
frame2_planets.grid(row=1, column=0, padx=10, pady=10, sticky=('N', 'W', 'E', 'S'))
frame3_gravity.grid(row=2, column=0, padx=10, pady=10, sticky=('N', 'W', 'E', 'S'))


# Create header text for each frame/application
label1_sports_header = ttk.Label(frame1_sports, text="Sports Analysis", font=("Helvetica", 10, "bold"))
label2_planets_header = ttk.Label(frame2_planets, text="Planetary Distance", font=("Helvetica", 10, "bold"))
label3_gravity_header = ttk.Label(frame3_gravity, text="Gravitational Pull", font=("Helvetica", 10, "bold"))


# Create description text that will sit below the headers and describe each application within each frame/application
label1_sports_desc = ttk.Label(frame1_sports, text="Use this application to track football match statistics", font=("Helvetica", 8, "normal"))
label2_planets_desc = ttk.Label(frame2_planets, text="Use this application to get distances to planets from earth.", font=("Helvetica", 8, "normal"))
label3_gravity_desc = ttk.Label(frame3_gravity, text="Use this application to calculate gravitational pull between objects.", font=("Helvetica", 8, "normal"))


# Place the header and description text labels in each frame at grid position row 0 column 0
label1_sports_header.grid(row=0, column=0, columnspan=3, padx=1, pady=5, sticky="w")
label2_planets_header.grid(row=0, column=0, columnspan=3, padx=1, pady=5, sticky="w")
label3_gravity_header.grid(row=0, column=0, columnspan=3, padx=1, pady=5, sticky="w")
label1_sports_desc.grid(row=1, column=0, columnspan=3, padx=1, pady=1, sticky="w, n")
label2_planets_desc.grid(row=1, column=0, columnspan=3, padx=1, pady=1, sticky="w, n")
label3_gravity_desc.grid(row=1, column=0, columnspan=3, padx=1, pady=1, sticky="w, n")


# Create Widgets and text for Date Time data
sports_day_label=ttk.Label(frame1_sports, text='Day:')
sports_day_label.grid(row=3, column=0, sticky='W')
sports_day_combo=ttk.Combobox(frame1_sports, values=[str(i) for i in range(1, 32)], state="readonly", width=3)
sports_day_combo.grid(row=4, column=0, sticky=('W'))

sports_month_label=ttk.Label(frame1_sports, text='Month:')
sports_month_label.grid(row=3, column=0, sticky='E')
sports_month_combo=ttk.Combobox(frame1_sports, values=[str(i) for i in range(1, 13)], state="readonly", width=3)
sports_month_combo.grid(row=4, column=0, sticky=('E'))

sports_year_label=ttk.Label(frame1_sports, text='Year:')
sports_year_label.grid(row=3, column=2, sticky='W')
sports_year_combo=ttk.Combobox(frame1_sports, values=('2024', '2025', '2026'), state="readonly", width=5)
sports_year_combo.grid(row=4, column=2, sticky=('W'))

sports_time_label=ttk.Label(frame1_sports, text='Time:')
sports_time_label.grid(row=3, column=3, sticky='W')
sports_time_combo=ttk.Combobox(frame1_sports, values=('09:00', '10:00', '11:00', '12:00', '13:00'), state="readonly", width=7)
sports_time_combo.grid(row=4, column=3, sticky=('W'))


# create widget objects for home team and away team data
sports_home_team_label= ttk.Label(frame1_sports, text='Home Team:')
sports_home_team_label.grid(row=5, column=0, sticky='W')
home_team_name = StringVar()
sports_home_team_entry= ttk.Entry(frame1_sports, textvariable=home_team_name)
sports_home_team_entry.grid(row=6, column=0, columnspan=1, sticky='w')


sports_away_team_label= ttk.Label(frame1_sports, text='Away Team:')
sports_away_team_label.grid(row=5, column=2, sticky='W')
away_team_name = StringVar()
sports_away_team_entry= ttk.Entry(frame1_sports, textvariable=away_team_name)
sports_away_team_entry.grid(row=6, column=2, columnspan=1, sticky='nsew')



# add separator 
separator_1=ttk.Separator(frame1_sports, orient='horizontal')
separator_1.grid(row=7, column=0, columnspan=3, padx=20, pady=20, sticky='w, n, e, s')

# descriptive text to explain how to use the click buttons in the next sections
sports_click_buttons_desc_text_label= tk.Label(frame1_sports,  wraplength=500, text='In the below sections click the appropriate button every time the relevant event occurs. These clicks will be totaled and displayed once the match has ended and providing relevant statistics for the game.')
sports_click_buttons_desc_text_label.grid(row=8, column=0, columnspan=4, padx=4, pady=5, sticky='W, E, S, N')


# create widget  for shots ON and Off Target
sports_shots_on_target_label= ttk.Label(frame1_sports, text='Shots On Target:')
sports_shots_on_target_label.grid(row=9, column=0, padx=5, pady=5,columnspan=2, sticky='w')
sports_shots_on_target=tk.Button(frame1_sports, text="Click For Every Shot on Target", padx=5, pady=5, wraplength=50, underline=True, background='white')
sports_shots_on_target.grid(row=10, column=0, padx=5, pady=5,columnspan=2, sticky='w')

sports_shots_off_target_label= ttk.Label(frame1_sports, text='Shots Off Target:')
sports_shots_off_target_label.grid(row=9, column=2, padx=5, pady=5,columnspan=2, sticky='w')
sports_shots_off_target=tk.Button(frame1_sports, text="Click for every Shot off Target", wraplength=50, underline=True, background='white' )
sports_shots_off_target.grid(row=10, column=2, padx=5, pady=5, columnspan=2, sticky='w')


# create widget  for Free Kicks for and Free Kicks Against
sports_free_kicks_for_label= ttk.Label(frame1_sports, text='Free Kicks - For:')
sports_free_kicks_for_label.grid(row=11, column=0, padx=5, pady=5,columnspan=2, sticky='w')
sports_free_kicks_for_button=tk.Button(frame1_sports, text="Click for every Free Kick For", wraplength=50, underline=True, background='white')
sports_free_kicks_for_button.grid(row=12, column=0, padx=5, pady=5,columnspan=2, sticky='w')

sports_free_kicks_against_label= ttk.Label(frame1_sports, text='Free Kicks  - Against:')
sports_free_kicks_against_label.grid(row=11, column=2, padx=5, pady=5,columnspan=2, sticky='w')
sports_free_kicks_against_button=tk.Button(frame1_sports, text="Click for every  Free Kick Against", wraplength=50, underline=True,background='white' )
sports_free_kicks_against_button.grid(row=12, column=2, padx=5, pady=5, columnspan=2, sticky='w')



# create widgets for Goals scored and conceded
sports_goals_scored_label= ttk.Label(frame1_sports, text='Goals - Scored:')
sports_goals_scored_label.grid(row=13, column=0, padx=5, pady=5,columnspan=2, sticky='w')
sports_goals_scored_button=tk.Button(frame1_sports, text="Click for every Goal Scored", wraplength=60, underline=True, background='white')
sports_goals_scored_button.grid(row=14, column=0, padx=5, pady=5,columnspan=2, sticky='w')

sports_goals_conceded_label= ttk.Label(frame1_sports, text='Goals - Conceded:')
sports_goals_conceded_label.grid(row=13, column=2, padx=5, pady=5,columnspan=2, sticky='w')
sports_goals_conceded_button=tk.Button(frame1_sports, text="Click for every Goal Conceded", wraplength=60, underline=True, background='white')
sports_goals_conceded_button.grid(row=14, column=2, padx=5, pady=5, columnspan=2, sticky='w')

# add separator 
separator_2=ttk.Separator(frame1_sports, orient='horizontal')
separator_2.grid(row=15, column=0, columnspan=3, padx=20, pady=20, sticky='w, n, e, s')

# # create text and button to finish match and display stats
sports_finished_match_label= tk.Label(frame1_sports, text='When the match has finished and you have finished collecting stats, click on the \'Finish\' button below to display collected match statistics.')
sports_finished_match_label.grid(row=16, column=0, padx=5, pady=5,columnspan=3, sticky='w')
sports_finished_match_button=tk.Button(frame1_sports, text="Finish", padx=5, pady=5, underline=True, background='white')
sports_finished_match_button.grid(row=17, column=1, padx=5, pady=5,columnspan=2, sticky='w')


# resizing config using grids weights and 
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame1_sports.columnconfigure(0, weight=3)
frame1_sports.columnconfigure(1, weight=3)
frame1_sports.columnconfigure(2, weight=3)
frame1_sports.columnconfigure(3, weight=3)
frame1_sports.columnconfigure(4, weight=3)
frame1_sports.rowconfigure(0, weight=3)
frame1_sports.rowconfigure(1, weight=3)
frame1_sports.rowconfigure(2, weight=3)
frame1_sports.rowconfigure(3, weight=3)
frame1_sports.rowconfigure(4, weight=3)
frame1_sports.rowconfigure(5, weight=3)
frame1_sports.rowconfigure(6, weight=3)
frame1_sports.rowconfigure(7, weight=3)
frame1_sports.rowconfigure(8, weight=3)
frame1_sports.rowconfigure(9, weight=3)
frame1_sports.rowconfigure(10, weight=3)
frame1_sports.rowconfigure(11, weight=3)
frame1_sports.rowconfigure(12, weight=3)
frame1_sports.rowconfigure(13, weight=3)
frame1_sports.rowconfigure(14, weight=3)

frame2_planets.columnconfigure(0, weight=3)
frame2_planets.rowconfigure(1, weight=4)

frame3_gravity.rowconfigure(1, weight=3)
frame3_gravity.columnconfigure(0, weight=3)

def home_team_valid(newvalue):
    return 
    


# Start the Tkinter event loop
root.mainloop()
