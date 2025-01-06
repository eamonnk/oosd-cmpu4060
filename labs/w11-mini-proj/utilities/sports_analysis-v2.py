import tkinter as tk
from tkinter import ttk
from tkinter import StringVar
import os
import csv
from pathlib import Path


# Create the main root window, this is the parent for each frame
# placed this first as getting errors if placed after functions
root = tk.Tk()
root.title("Mini project - 3 applications - Jan 2025")




# define control variables to track click button values and counts, set default values at zero
shots_on_target_intvar=tk.IntVar(value='0')
shots_off_target_intvar=tk.IntVar(value='0')
free_kicks_for_intvar=tk.IntVar(value='0')
free_kicks_against_intvar=tk.IntVar(value='0')
goals_for_intvar=tk.IntVar(value='0')
goals_against_intvar=tk.IntVar(value='0')


# define StringVar() string variables - do here outside of functions
sports_sont_string_and_realtime_intvar=StringVar() # shots_on_target=sont
sports_sofft_string_and_realtime_intvar=StringVar() # shots_off_target = sofft
sports_fkf_string_and_realtime_intvar=StringVar()  # free_kicks_for = fkf
sports_fka_string_and_realtime_intvar=StringVar() # free_kicks_against = fka
sports_gf_string_and_realtime_intvar=StringVar() # goals_for=gf
sports_ga_string_and_realtime_intvar=StringVar()  # goals_against=ga



# create function to create csv file, used some references belwotpo make sure it ges created 
# in same location as current .py file
# https://docs.python.org/3/library/os.path.html ++ https://sqlpey.com/python/top-10-methods-to-retrieve-full-path/
py_file_location=os.path.dirname(os.path.realpath(__file__))
csv_file_name="match_analysis.csv"
csv_file_name_and_path=os.path.join(py_file_location, csv_file_name)

csv_file_headers=[
    'date', 'month', 'year', 'ko_time', 'home_team', 'away_team',
    'shots_on_target', 'shots_off_target', 'free_kicks_for', 
    'free_kicks_against', 'goals_for', 'goals_against'
]

#function to create the csv file, check if it exists or not and create if not exists
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

# function to define functionality when shots ontarget button is clicked
# we use IntVar() as a dynamic variable that is updated inside the utility at tun time oin each click
def shots_on_target_click():
    #intvar get() method gets the current value, we defined this as '0' earlier
    shots_on_target_current_value=shots_on_target_intvar.get()
    # we set a new value for the variable as the current value + 1
    shots_on_target_intvar.set(shots_on_target_current_value + 1)
    # we define a variable value with string that we will call in the utility to display the updated value to the user at run time
    sports_sont_string_and_realtime_intvar.set("Total: {} ".format(shots_on_target_intvar.get()))
    # we just print the output during runtime so we can see it is working fine
    print("Shots on Target: {}".format(shots_on_target_intvar.get()))
    
def shots_off_target_click():
    shots_off_target_current_value=shots_off_target_intvar.get()
    shots_off_target_intvar.set(shots_off_target_current_value + 1)
    sports_sofft_string_and_realtime_intvar.set("Total: {} ".format(shots_off_target_intvar.get()))
    print("Shots off Target: {}".format(shots_off_target_intvar.get()))
    
def free_kicks_for_click():
    free_kicks_for_current_value=free_kicks_for_intvar.get()
    free_kicks_for_intvar.set(free_kicks_for_current_value + 1)
    sports_fkf_string_and_realtime_intvar.set("Total: {} ".format(free_kicks_for_intvar.get()))
    print("Free Kicks for: {}".format(free_kicks_for_intvar.get()))
    
def free_kicks_against_click():
    free_kicks_against_current_value=free_kicks_against_intvar.get()
    free_kicks_against_intvar.set(free_kicks_against_current_value + 1)
    sports_fka_string_and_realtime_intvar.set("Total: {} ".format(free_kicks_against_intvar.get()))
    print("Free Kicks Against: {}".format(free_kicks_against_intvar.get())) 
        
def goals_for_click():
    goals_for_current_value=goals_for_intvar.get()
    goals_for_intvar.set(goals_for_current_value + 1)
    sports_gf_string_and_realtime_intvar.set("Total: {} ".format(goals_for_intvar.get()))
    print("Goals For: {}".format(goals_for_intvar.get()))

def goals_against_click():
    goals_against_current_value=goals_against_intvar.get()
    goals_against_intvar.set(goals_against_current_value + 1)
    sports_ga_string_and_realtime_intvar.set("Total: {} ".format(goals_against_intvar.get()))
    print("Goals Against: {}".format(goals_against_intvar.get()))

# when finish button clicked - function to replace initial existing data collection frame 
# with new results frame
def sports_replace_frame():
    # read data from csv file and place in dictionary
    with open(csv_file_name_and_path, 'r') as file:
        reader=list(csv.reader(file)) # read all rows as a list
        headers=reader[0]
        last_row=reader[-1]
    #create dictionary by zipping two lists together
    csv_results_dict=dict(zip(headers, last_row))
    print(csv_results_dict)
    
    # get rid of the initial data collection frame > https://tkdocs.com/shipman/event-types.html
    frame1_sports.destroy()
    
    # create a new frame to display the finiahed collected data and place it using .grid()
    frame1a_sports_finished = tk.Frame(root, borderwidth=2, relief="groove", padx=5, pady=10)
    frame1a_sports_finished.grid(row=0, column=0, padx=10, pady=10, sticky=('N', 'W', 'E', 'S'))
    
    #create header and description labels and then place them using grid()
    label1a_sports_finished_header = tk.Label(frame1a_sports_finished, text="Sports Analysis - Finished Results", font=("Helvetica", 10, "bold"))
    label1a_sports_finished_desc = ttk.Label(frame1a_sports_finished, text="The following is the data collected for your match", font=("Helvetica", 8, "normal"))
    label1a_sports_finished_header.grid(row=0, column=0, columnspan=3, padx=1, pady=5, sticky="w")
    label1a_sports_finished_desc.grid(row=1, column=0, columnspan=3, padx=1, pady=1, sticky="w, n")
    
    # add separator 
    separator_3=ttk.Separator(frame1a_sports_finished, orient='horizontal')
    separator_3.grid(row=2, column=0, columnspan=3, padx=20, pady=20, sticky='w, n, e, s')
    
    # create the display strings for data using dictionary key value pairs
    # we will call these in the widget and place them in the grid
    results_teams_str="{} vs  {}".format(csv_results_dict['home_team'], csv_results_dict['away_team'])
    results_date_str="{}/{}/{}".format((csv_results_dict['date']), (csv_results_dict['month']), (csv_results_dict['year']))
    results_ko_time_str="KO Time: {}".format(csv_results_dict['ko_time'])
    results_shots_str="Shots -   On Target: {}   Off Target: {}".format(csv_results_dict['shots_on_target'], csv_results_dict['shots_off_target'])
    results_free_kicks_str="Free Kicks -   For: {}   Against: {}".format(csv_results_dict['free_kicks_for'], csv_results_dict['free_kicks_against'])
    results_goals_str="Goals -   For: {}   Against: {}".format(csv_results_dict['goals_for'], csv_results_dict['goals_against'])
    
    # team, date and KO time widgets
    results_teams_str_label=tk.Label(frame1a_sports_finished, text=results_teams_str)
    results_teams_str_label.grid(row=3, column=1, columnspan=3, padx=1, pady=1)
    results_date_str_label=tk.Label(frame1a_sports_finished, text=results_date_str)
    results_date_str_label.grid(row=4, column=1, columnspan=3)
    results_ko_time_label=tk.Label(frame1a_sports_finished, text=results_ko_time_str)
    results_ko_time_label.grid(row=5, column=1, columnspan=3)
    
    # add separator - just to demarcate macro data and 
    separator_4=ttk.Separator(frame1a_sports_finished, orient='horizontal')
    separator_4.grid(row=6, column=0, columnspan=4, padx=20, pady=20, sticky='w, n, e, s')
    
    # shots, free kicks and goal widgets
    results_shots_str_label=tk.Label(frame1a_sports_finished, text=results_shots_str)
    results_shots_str_label.grid(row=7, column=1, columnspan=3)
    results_free_kicks_str_label=tk.Label(frame1a_sports_finished, text=results_free_kicks_str)
    results_free_kicks_str_label.grid(row=8, column=1, columnspan=3)
    results_goals_str_label=tk.Label(frame1a_sports_finished, text=results_goals_str)
    results_goals_str_label.grid(row=9, column=1, columnspan=3)
    
    #re-sizing
    frame1a_sports_finished.columnconfigure(0, weight=3)
    frame1a_sports_finished.columnconfigure(1, weight=3)
    frame1a_sports_finished.columnconfigure(2, weight=3)
    frame1a_sports_finished.columnconfigure(3, weight=3)
    frame1a_sports_finished.columnconfigure(4, weight=3)
    frame1a_sports_finished.rowconfigure(0, weight=3)
    frame1a_sports_finished.rowconfigure(1, weight=3)
    frame1a_sports_finished.rowconfigure(2, weight=3)
    frame1a_sports_finished.rowconfigure(3, weight=3)
    frame1a_sports_finished.rowconfigure(4, weight=3)
    frame1a_sports_finished.rowconfigure(5, weight=3)
    frame1a_sports_finished.rowconfigure(6, weight=3)
    frame1a_sports_finished.rowconfigure(7, weight=3)
    frame1a_sports_finished.rowconfigure(8, weight=3)
    frame1a_sports_finished.rowconfigure(9, weight=3)

    
    
# when click finish button we need to write all the data to the earlier created csv file
# we will then read the last row and headers from the csv file and store that data in s dictionary in key value pairs
# then get rid of old frame and call a new frame which will display the stats
def finish_button_click():
    # get data from widgets using the .get method to return the current value of the widget and store them as variables
    date=sports_day_combo.get()
    month=sports_month_combo.get()
    year=sports_year_combo.get()
    ko_time=sports_time_combo.get()
    home_team=sports_home_team_entry.get()
    away_team=sports_away_team_entry.get()
    
    # write data to csv file
    # we use 'with' statement so we don't have to close the file afterwards
    with open(csv_file_name_and_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, month, year, ko_time, home_team, away_team, shots_on_target_intvar.get(), shots_off_target_intvar.get(), free_kicks_for_intvar.get(), free_kicks_against_intvar.get(), goals_for_intvar.get(), goals_against_intvar.get()
                         ])

    sports_replace_frame()

# Create 3 separate frames with borders, one for each of the 3 applications, so we can demarcate between them.
# we have a second one for sports analysis as there will be a results frame to display the final stats when finished
frame1_sports = tk.Frame(root, borderwidth=2, relief="groove", padx=5, pady=10)
frame2_planets = tk.Frame(root, borderwidth=2, relief="groove", padx=5, pady=10)
frame3_gravity = tk.Frame(root, borderwidth=2, relief="groove", padx=5, pady=10)


# Place the frames in the main window using grids with some padding between them and align west
# we will not place the sports_finished frame here, it will be called in a function
frame1_sports.grid(row=0, column=0, padx=10, pady=10, sticky=('N', 'W', 'E', 'S'))
frame2_planets.grid(row=1, column=0, padx=10, pady=10, sticky=('N', 'W', 'E', 'S'))
frame3_gravity.grid(row=2, column=0, padx=10, pady=10, sticky=('N', 'W', 'E', 'S'))


# Create header text for each frame/application
label1_sports_header = tk.Label(frame1_sports, text="Sports Analysis", font=("Helvetica", 10, "bold"))
label2_planets_header = tk.Label(frame2_planets, text="Planetary Distance", font=("Helvetica", 10, "bold"))
label3_gravity_header = tk.Label(frame3_gravity, text="Gravitational Pull", font=("Helvetica", 10, "bold"))


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
sports_day_label=ttk.Label(frame1_sports, text='Date:')
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

sports_time_label=ttk.Label(frame1_sports, text='Kick Off Time:')
sports_time_label.grid(row=3, column=3, sticky='W')
sports_time_combo=ttk.Combobox(frame1_sports, values=('09:00', '10:00', '11:00', '12:00', '13:00', '14:00'), state="readonly", width=10)
sports_time_combo.grid(row=4, column=3, sticky=('W'))


# create widget objects for home team and away team data
sports_home_team_label= ttk.Label(frame1_sports, text='Home Team:')
sports_home_team_label.grid(row=5, column=0, sticky='W')
home_team_name = StringVar()
sports_home_team_entry= ttk.Entry(frame1_sports)
sports_home_team_entry.grid(row=6, column=0, columnspan=1, sticky='w')
# sports_home_team_entry= ttk.Entry(frame1_sports, textvariable=home_team_name)
# sports_home_team_entry.grid(row=6, column=0, columnspan=1, sticky='w')


sports_away_team_label= ttk.Label(frame1_sports, text='Away Team:')
sports_away_team_label.grid(row=5, column=2, sticky='W')
away_team_name = StringVar()
sports_away_team_entry= ttk.Entry(frame1_sports)
sports_away_team_entry.grid(row=6, column=2, columnspan=1, sticky='nsew')
# sports_away_team_entry= ttk.Entry(frame1_sports, textvariable=away_team_name)
# sports_away_team_entry.grid(row=6, column=2, columnspan=1, sticky='nsew')


# add separator 
separator_1=ttk.Separator(frame1_sports, orient='horizontal')
separator_1.grid(row=7, column=0, columnspan=3, padx=20, pady=20, sticky='w, n, e, s')

# descriptive text to explain how to use the click buttons in the next sections
sports_click_buttons_desc_text_label= tk.Label(frame1_sports,  wraplength=500, text='In the below sections click the appropriate button every time the relevant event occurs. These clicks will be totaled and displayed once the match has ended and providing relevant statistics for the game.')
sports_click_buttons_desc_text_label.grid(row=8, column=0, columnspan=4, padx=4, pady=5, sticky='W, E, S, N')


# create widget  for shots ON and Off Target
sports_shots_on_target_label= ttk.Label(frame1_sports, text='Shots On Target:')
sports_shots_on_target_label.grid(row=9, column=0, padx=5, pady=5,columnspan=2, sticky='w')
sports_shots_on_target=tk.Button(frame1_sports, text="Click For Every Shot on Target", padx=5, pady=5, wraplength=50, underline=True, background='white', command=shots_on_target_click)
sports_shots_on_target.grid(row=10, column=0, padx=5, pady=5,columnspan=2, sticky='w')

sports_shots_off_target_label= ttk.Label(frame1_sports, text='Shots Off Target:')
sports_shots_off_target_label.grid(row=9, column=2, padx=5, pady=5,columnspan=2, sticky='w')
sports_shots_off_target=tk.Button(frame1_sports, text="Click for every Shot off Target", wraplength=50, underline=True, background='white', command=shots_off_target_click)
sports_shots_off_target.grid(row=10, column=2, padx=5, pady=5, columnspan=2, sticky='w')


# create widget  for Free Kicks for and Free Kicks Against
sports_free_kicks_for_label= ttk.Label(frame1_sports, text='Free Kicks - For:')
sports_free_kicks_for_label.grid(row=11, column=0, padx=5, pady=5,columnspan=2, sticky='w')
sports_free_kicks_for_button=tk.Button(frame1_sports, text="Click for every Free Kick For", wraplength=50, underline=True, background='white', command=free_kicks_for_click)
sports_free_kicks_for_button.grid(row=12, column=0, padx=5, pady=5,columnspan=2, sticky='w')

sports_free_kicks_against_label= ttk.Label(frame1_sports, text='Free Kicks  - Against:')
sports_free_kicks_against_label.grid(row=11, column=2, padx=5, pady=5,columnspan=2, sticky='w')
sports_free_kicks_against_button=tk.Button(frame1_sports, text="Click for every Free Kick Against", wraplength=50, underline=True,background='white',command=free_kicks_against_click)
sports_free_kicks_against_button.grid(row=12, column=2, padx=5, pady=5, columnspan=2, sticky='w')



# create widgets for Goals scored and conceded
sports_goals_scored_label= ttk.Label(frame1_sports, text='Goals - Scored:')
sports_goals_scored_label.grid(row=13, column=0, padx=5, pady=5,columnspan=2, sticky='w')
sports_goals_scored_button=tk.Button(frame1_sports, text="Click for every Goal Scored", wraplength=60, underline=True, background='white', command=goals_for_click)
sports_goals_scored_button.grid(row=14, column=0, padx=5, pady=5,columnspan=2, sticky='w')

sports_goals_conceded_label= ttk.Label(frame1_sports, text='Goals - Conceded:')
sports_goals_conceded_label.grid(row=13, column=2, padx=5, pady=5,columnspan=2, sticky='w')
sports_goals_conceded_button=tk.Button(frame1_sports, text="Click for every Goal Conceded", wraplength=60, underline=True, background='white', command=goals_against_click)
sports_goals_conceded_button.grid(row=14, column=2, padx=5, pady=5, columnspan=2, sticky='w')

# add separator 
separator_2=ttk.Separator(frame1_sports, orient='horizontal')
separator_2.grid(row=15, column=0, columnspan=3, padx=20, pady=20, sticky='w, n, e, s')

# # create text and button to finish match and display stats
sports_finished_match_label= tk.Label(frame1_sports, text='When the match has finished and you have finished collecting stats, click on the \'Finish\' button below to display collected match statistics.')
sports_finished_match_label.grid(row=16, column=0, padx=5, pady=5,columnspan=3, sticky='w')
sports_finished_match_button=tk.Button(frame1_sports, text="Finish", padx=5, pady=5, underline=True, background='white', command=finish_button_click)
sports_finished_match_button.grid(row=17, column=1, padx=5, pady=5,columnspan=2, sticky='w')



# here------
# create widgets to display realtime intvar() values, so user knows it is working and 
# can see in realtime what the values are
sports_sont_intvar_current_value_label=tk.Label(frame1_sports, textvariable=sports_sont_string_and_realtime_intvar)
sports_sont_intvar_current_value_label.grid(row=10, column=0, sticky='e')
sports_sofft_intvar_current_value_label=tk.Label(frame1_sports, textvariable=sports_sofft_string_and_realtime_intvar)
sports_sofft_intvar_current_value_label.grid(row=10, column=2, sticky='e')
sports_fkf_intvar_current_value_label=tk.Label(frame1_sports, textvariable=sports_fkf_string_and_realtime_intvar)
sports_fkf_intvar_current_value_label.grid(row=12, column=0, sticky='e')
sports_fka_intvar_current_value_label=tk.Label(frame1_sports, textvariable=sports_fka_string_and_realtime_intvar)
sports_fka_intvar_current_value_label.grid(row=12, column=2, sticky='e')
sports_gf_intvar_current_value_label=tk.Label(frame1_sports, textvariable=sports_gf_string_and_realtime_intvar)
sports_gf_intvar_current_value_label.grid(row=14, column=0, sticky='e')
sports_ga_intvar_current_value_label=tk.Label(frame1_sports, textvariable=sports_ga_string_and_realtime_intvar)
sports_ga_intvar_current_value_label.grid(row=14, column=2, sticky='e')



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
    

# Start the Tkinter event loop
root.mainloop()
