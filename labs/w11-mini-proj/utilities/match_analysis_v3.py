import tkinter as tk # used for tk works
from tkinter import ttk # some ttk widgets used
from tkinter import StringVar
import os # used for filer and path work
import csv # used for csv file work
from pathlib import Path



class match_analysis:

# Create the main root window, this is the parent for each frame
# placed this first as getting errors if placed after functions
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Mini project - 3 applications - Jan 2025")

        # define tkinter control variables as instance variabgles to track click button values and counts, set default values at zero
        self.shots_on_target_intvar=tk.IntVar(value='0')
        self.shots_off_target_intvar=tk.IntVar(value='0')
        self.free_kicks_for_intvar=tk.IntVar(value='0')
        self.free_kicks_against_intvar=tk.IntVar(value='0')
        self.goals_for_intvar=tk.IntVar(value='0')
        self.goals_against_intvar=tk.IntVar(value='0')


        # define StringVar() string variables - do here in constructor so they are available as instance variables to other functions
        self.sports_sont_string_and_realtime_intvar=StringVar() # shots_on_target=sont
        self.sports_sofft_string_and_realtime_intvar=StringVar() # shots_off_target = sofft
        self.sports_fkf_string_and_realtime_intvar=StringVar()  # free_kicks_for = fkf
        self.sports_fka_string_and_realtime_intvar=StringVar() # free_kicks_against = fka
        self.sports_gf_string_and_realtime_intvar=StringVar() # goals_for=gf
        self.sports_ga_string_and_realtime_intvar=StringVar()  # goals_against=ga


        # create csv file, used some references below to make sure it gets created 
        # in same location as current .py file
        # https://docs.python.org/3/library/os.path.html ++ https://sqlpey.com/python/top-10-methods-to-retrieve-full-path/
        # self.py_file_location=os.path.dirname(os.path.realpath(__file__))
        # self.csv_file_name="match_analysis.csv"
        # self.csv_file_name_and_path=os.path.join(self.py_file_location, self.csv_file_name)
        # # list of headers we will use and track data for in csv file from app usage
        # self.csv_file_headers=[
        #     'date', 'month', 'year', 'ko_time', 'home_team', 'away_team',
        #     'shots_on_target', 'shots_off_target', 'free_kicks_for', 
        #     'free_kicks_against', 'goals_for', 'goals_against'
        # ]

        
        # Create frame with border
        # we create a second frame later for displaying final stats, that is created and managed in a separate function
        self.frame1_sports = tk.Frame(self.root, borderwidth=2, relief="groove", padx=5, pady=10)

        # Place the frame grids() with some padding between them and align west
        # we will not place the sports_finished frame here, it will be called in a function
        self.frame1_sports.grid(row=0, column=0, padx=10, pady=10, sticky=('N', 'W', 'E', 'S'))

        # Create header text for frame
        self.label1_sports_header = tk.Label(self.frame1_sports, text="Match Analysis - Data Collection", font=("Helvetica", 10, "bold"))

        # Create description text that will sit below the header and describe each application within the frame
        self.label1_sports_desc = ttk.Label(self.frame1_sports, text="Use this application to track football match statistics", font=("Helvetica", 8, "normal"))

        # Place the header and description text labels in each frame at grid position row 0 column 0
        self.label1_sports_header.grid(row=0, column=0, columnspan=3, padx=1, pady=5, sticky="w")
        self.label1_sports_desc.grid(row=1, column=0, columnspan=3, padx=1, pady=1, sticky="w, n")

        # calls create csv file function
        self.csv_file_create()

    # function to create the csv file, check if it exists or not and create if not exists
    def csv_file_create(self):
        
        # create csv file, used some references below to make sure it gets created 
        # in same location as current .py file
        # https://docs.python.org/3/library/os.path.html ++ https://sqlpey.com/python/top-10-methods-to-retrieve-full-path/
        self.py_file_location=os.path.dirname(os.path.realpath(__file__))
        # define csv file name to store data. could prompt user for its name and define outside of function but it is not used, seen or interacted with user in the app so just lf it hard coded here 
        self.csv_file_name="match_analysis.csv"
        self.csv_file_name_and_path=os.path.join(self.py_file_location, self.csv_file_name)
        # list of headers we will use and track data for in csv file from app usage.hard coded here as no user interaction with the file
        # and keeps it all self contained
        self.csv_file_headers=[
            'date', 'month', 'year', 'ko_time', 'home_team', 'away_team',
            'shots_on_target', 'shots_off_target', 'free_kicks_for', 
            'free_kicks_against', 'goals_for', 'goals_against'
        ]
        
        # check if it exists already, open it and write toit        
        if not os.path.isfile(self.csv_file_name_and_path):
            with open(self.csv_file_name_and_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(self.csv_file_headers)
            print(" csv file {} created with headers. ".format(self.csv_file_name))        
        
        else:
            print(" csv file already exists. ".format(self.csv_file_name))
            dir=os.path.dirname
            print(dir)
            
            self.create_widgets()
        

    def create_widgets(self):
            # Create Widgets and text for Date Time data
            self.sports_day_label=ttk.Label(self.frame1_sports, text='Date:')
            self.sports_day_label.grid(row=3, column=0, sticky='W')
            self.sports_day_combo=ttk.Combobox(self.frame1_sports, values=[str(i) for i in range(1, 32)], state="readonly", width=3)
            self.sports_day_combo.grid(row=4, column=0, sticky=('W'))

            self.sports_month_label=ttk.Label(self.frame1_sports, text='Month:')
            self.sports_month_label.grid(row=3, column=0, sticky='E')
            self.sports_month_combo=ttk.Combobox(self.frame1_sports, values=[str(i) for i in range(1, 13)], state="readonly", width=3)
            self.sports_month_combo.grid(row=4, column=0, sticky=('E'))

            self.sports_year_label=ttk.Label(self.frame1_sports, text='Year:')
            self.sports_year_label.grid(row=3, column=2, sticky='W')
            self.sports_year_combo=ttk.Combobox(self.frame1_sports, values=('2024', '2025', '2026'), state="readonly", width=5)
            self.sports_year_combo.grid(row=4, column=2, sticky=('W'))

            self.sports_time_label=ttk.Label(self.frame1_sports, text='Kick Off Time:')
            self.sports_time_label.grid(row=3, column=3, sticky='W')
            self.sports_time_combo=ttk.Combobox(self.frame1_sports, values=('09:00', '10:00', '11:00', '12:00', '13:00', '14:00'), state="readonly", width=10)
            self.sports_time_combo.grid(row=4, column=3, sticky=('W'))


            # create widget objects for home team and away team data
            self.sports_home_team_label= ttk.Label(self.frame1_sports, text='Home Team:')
            self.sports_home_team_label.grid(row=5, column=0, sticky='W')
            self.home_team_name = StringVar()
            self.sports_home_team_entry= ttk.Entry(self.frame1_sports)
            self.sports_home_team_entry.grid(row=6, column=0, columnspan=1, sticky='w')


            self.sports_away_team_label= ttk.Label(self.frame1_sports, text='Away Team:')
            self.sports_away_team_label.grid(row=5, column=2, sticky='W')
            self.away_team_name = StringVar()
            self.sports_away_team_entry= ttk.Entry(self.frame1_sports)
            self.sports_away_team_entry.grid(row=6, column=2, columnspan=1, sticky='nsew')


            # add separator 
            separator_1=ttk.Separator(self.frame1_sports, orient='horizontal')
            separator_1.grid(row=7, column=0, columnspan=3, padx=20, pady=20, sticky='w, n, e, s')

            # descriptive text to explain how to use the click buttons in the next sections
            self.sports_click_buttons_desc_text_label= tk.Label(self.frame1_sports,  wraplength=500, text='In the below sections click the appropriate button every time the relevant event occurs. These clicks will be totaled and displayed once the match has ended and providing relevant statistics for the game.')
            self.sports_click_buttons_desc_text_label.grid(row=8, column=0, columnspan=4, padx=4, pady=5, sticky='W, E, S, N')

            # create widget  for shots ON and Off Target
            self.sports_shots_on_target_label= ttk.Label(self.frame1_sports, text='Shots On Target:')
            self.sports_shots_on_target_label.grid(row=9, column=0, padx=5, pady=5,columnspan=2, sticky='w')
            self.sports_shots_on_target=tk.Button(self.frame1_sports, text="Click For Every Shot on Target", padx=5, pady=5, wraplength=50, underline=True, background='white', command=self.shots_on_target_click)
            self.sports_shots_on_target.grid(row=10, column=0, padx=5, pady=5,columnspan=2, sticky='w')

            self.sports_shots_off_target_label= ttk.Label(self.frame1_sports, text='Shots Off Target:')
            self.sports_shots_off_target_label.grid(row=9, column=2, padx=5, pady=5,columnspan=2, sticky='w')
            self.sports_shots_off_target=tk.Button(self.frame1_sports, text="Click for every Shot off Target", wraplength=50, underline=True, background='white', command=self.shots_off_target_click)
            self.sports_shots_off_target.grid(row=10, column=2, padx=5, pady=5, columnspan=2, sticky='w')


            # create widget  for Free Kicks for and Free Kicks Against
            sports_free_kicks_for_label= ttk.Label(self.frame1_sports, text='Free Kicks - For:')
            sports_free_kicks_for_label.grid(row=11, column=0, padx=5, pady=5,columnspan=2, sticky='w')
            sports_free_kicks_for_button=tk.Button(self.frame1_sports, text="Click for every Free Kick For", wraplength=50, underline=True, background='white', command=self.free_kicks_for_click)
            sports_free_kicks_for_button.grid(row=12, column=0, padx=5, pady=5,columnspan=2, sticky='w')

            sports_free_kicks_against_label= ttk.Label(self.frame1_sports, text='Free Kicks  - Against:')
            sports_free_kicks_against_label.grid(row=11, column=2, padx=5, pady=5,columnspan=2, sticky='w')
            sports_free_kicks_against_button=tk.Button(self.frame1_sports, text="Click for every Free Kick Against", wraplength=50, underline=True,background='white',command=self.free_kicks_against_click)
            sports_free_kicks_against_button.grid(row=12, column=2, padx=5, pady=5, columnspan=2, sticky='w')


            # create widgets for Goals scored (For) and conceded (Against)
            sports_goals_scored_label= ttk.Label(self.frame1_sports, text='Goals - For:')
            sports_goals_scored_label.grid(row=13, column=0, padx=5, pady=5,columnspan=2, sticky='w')
            sports_goals_scored_button=tk.Button(self.frame1_sports, text="Click for every Goal Scored", wraplength=60, underline=True, background='white', command=self.goals_for_click)
            sports_goals_scored_button.grid(row=14, column=0, padx=5, pady=5,columnspan=2, sticky='w')

            sports_goals_conceded_label= ttk.Label(self.frame1_sports, text='Goals - Against:')
            sports_goals_conceded_label.grid(row=13, column=2, padx=5, pady=5,columnspan=2, sticky='w')
            sports_goals_conceded_button=tk.Button(self.frame1_sports, text="Click for every Goal Conceded", wraplength=60, underline=True, background='white', command=self.goals_against_click)
            sports_goals_conceded_button.grid(row=14, column=2, padx=5, pady=5, columnspan=2, sticky='w')

            # add separator 
            separator_2=ttk.Separator(self.frame1_sports, orient='horizontal')
            separator_2.grid(row=15, column=0, columnspan=3, padx=20, pady=20, sticky='w, n, e, s')

            # # create text and button to finish match and display stats
            sports_finished_match_label= tk.Label(self.frame1_sports, text='When the match has finished and you have finished collecting stats, click on the \'Finish\' button below to display collected match statistics.')
            sports_finished_match_label.grid(row=16, column=0, padx=5, pady=5,columnspan=3, sticky='w')
            sports_finished_match_button=tk.Button(self.frame1_sports, text="Finish", padx=5, pady=5, underline=True, background='white', command=self.finish_button_click)
            sports_finished_match_button.grid(row=17, column=0, padx=10, pady=5, sticky='e')
            
            # create User Guide button and place it using grid()
            sports_frame1_user_guide_button=tk.Button(self.frame1_sports,text="User Guide", padx=5, pady=5, underline=True, background='white', command=self.user_guide_button_click)
            sports_frame1_user_guide_button.grid(row=17, column=2, padx=10, pady=5, sticky='w')
            
            
            # resizing initial first frame config using grid weights 
            self.root.columnconfigure(0, weight=1)
            self.root.rowconfigure(0, weight=1)
            self.frame1_sports.columnconfigure(0, weight=3)
            self.frame1_sports.columnconfigure(1, weight=3)
            self.frame1_sports.columnconfigure(2, weight=3)
            self.frame1_sports.columnconfigure(3, weight=3)
            self.frame1_sports.columnconfigure(4, weight=3)
            self.frame1_sports.rowconfigure(0, weight=3)
            self.frame1_sports.rowconfigure(1, weight=3)
            self.frame1_sports.rowconfigure(2, weight=3)
            self.frame1_sports.rowconfigure(3, weight=3)
            self.frame1_sports.rowconfigure(4, weight=3)
            self.frame1_sports.rowconfigure(5, weight=3)
            self.frame1_sports.rowconfigure(6, weight=3)
            self.frame1_sports.rowconfigure(7, weight=3)
            self.frame1_sports.rowconfigure(8, weight=3)
            self.frame1_sports.rowconfigure(9, weight=3)
            self.frame1_sports.rowconfigure(10, weight=3)
            self.frame1_sports.rowconfigure(11, weight=3)
            self.frame1_sports.rowconfigure(12, weight=3)
            self.frame1_sports.rowconfigure(13, weight=3)
            self.frame1_sports.rowconfigure(14, weight=3)    
        
        
            self.realtime_intvar_values()



    # function to define functionality when shots ontarget button is clicked
    # we use IntVar() as a dynamic variable that is updated inside the utility at tun time oin each click
    def shots_on_target_click(self):
        #intvar get() method gets the current value, we defined this as '0' earlier
        self.shots_on_target_current_value=self.shots_on_target_intvar.get()
        # we set a new value for the variable as the current value + 1
        self.shots_on_target_intvar.set(self.shots_on_target_current_value + 1)
        # we define a variable value with string that we will call in the utility to display the updated value to the user at run time
        self.sports_sont_string_and_realtime_intvar.set("Total: {} ".format(self.shots_on_target_intvar.get()))
        # we just print the output during runtime so we can see it is working fine
        print("Shots on Target: {}".format(self.shots_on_target_intvar.get()))
    
    # same as above for next stat to track
    def shots_off_target_click(self):
        self.shots_off_target_current_value=self.shots_off_target_intvar.get()
        self.shots_off_target_intvar.set(self.shots_off_target_current_value + 1)
        self.sports_sofft_string_and_realtime_intvar.set("Total: {} ".format(self.shots_off_target_intvar.get()))
        print("Shots off Target: {}".format(self.shots_off_target_intvar.get()))
    
    # same as above for next stat to track    
    def free_kicks_for_click(self):
        self.free_kicks_for_current_value=self.free_kicks_for_intvar.get()
        self.free_kicks_for_intvar.set(self.free_kicks_for_current_value + 1)
        self.sports_fkf_string_and_realtime_intvar.set("Total: {} ".format(self.free_kicks_for_intvar.get()))
        print("Free Kicks for: {}".format(self.free_kicks_for_intvar.get()))
    
    # same as above for next stat to track
    def free_kicks_against_click(self):
        self.free_kicks_against_current_value=self.free_kicks_against_intvar.get()
        self.free_kicks_against_intvar.set(self.free_kicks_against_current_value + 1)
        self.sports_fka_string_and_realtime_intvar.set("Total: {} ".format(self.free_kicks_against_intvar.get()))
        print("Free Kicks Against: {}".format(self.free_kicks_against_intvar.get())) 
    
    # same as above for next stat to track    
    def goals_for_click(self):
        self.goals_for_current_value=self.goals_for_intvar.get()
        self.goals_for_intvar.set(self.goals_for_current_value + 1)
        self.sports_gf_string_and_realtime_intvar.set("Total: {} ".format(self.goals_for_intvar.get()))
        print("Goals For: {}".format(self.goals_for_intvar.get()))

    # same as above for next stat to track
    def goals_against_click(self):
        self.goals_against_current_value=self.goals_against_intvar.get()
        self.goals_against_intvar.set(self.goals_against_current_value + 1)
        self.sports_ga_string_and_realtime_intvar.set("Total: {} ".format(self.goals_against_intvar.get()))
        print("Goals Against: {}".format(self.goals_against_intvar.get()))

    # when finish button clicked - function to replace initial existing data collection frame 
    # with new results frame
    def sports_replace_frame(self):
        # read data from csv file and place in dictionary
        with open(self.csv_file_name_and_path, 'r') as file:
            reader=list(csv.reader(file)) # read all rows as a list
            headers=reader[0]
            last_row=reader[-1]
        #create dictionary by zipping two lists together
        self.csv_results_dict=dict(zip(headers, last_row))
        print(self.csv_results_dict)
        
        # get rid of the initial data collection frame > https://tkdocs.com/shipman/event-types.html
        self.frame1_sports.destroy()
        
        # create a new frame to display the finiahed collected data and place it using .grid()
        self.frame1a_sports_finished = tk.Frame(self.root, borderwidth=2, relief="groove", padx=5, pady=10)
        self.frame1a_sports_finished.grid(row=0, column=0, padx=10, pady=10, sticky="w, n")
        
        #create header and description labels and then place them using grid()
        label1a_sports_finished_header = tk.Label(self.frame1a_sports_finished, text="Match Analysis - Finished Results", font=("Helvetica", 10, "bold"))
        label1a_sports_finished_desc = ttk.Label(self.frame1a_sports_finished, text="The following is the data collected for your match", font=("Helvetica", 8, "normal"))
        label1a_sports_finished_header.grid(row=0, column=0, columnspan=3, padx=1, pady=5, sticky="w")
        label1a_sports_finished_desc.grid(row=1, column=0, columnspan=3, padx=1, pady=1, sticky="w, n")
        
        # add separator 
        separator_3=ttk.Separator(self.frame1a_sports_finished, orient='horizontal')
        separator_3.grid(row=2, column=0, columnspan=3, padx=20, pady=20, sticky='w, n, e, s')
        
        # create the display strings for data using dictionary key value pairs
        # we will call these in the widget and place them in the grid
        results_teams_str="{} vs  {}".format(self.csv_results_dict['home_team'], self.csv_results_dict['away_team'])
        results_date_str="{}/{}/{}".format((self.csv_results_dict['date']), (self.csv_results_dict['month']), (self.csv_results_dict['year']))
        results_ko_time_str="KO Time: {}".format(self.csv_results_dict['ko_time'])
        results_shots_str="Shots -   On Target: {}   Off Target: {}".format(self.csv_results_dict['shots_on_target'], self.csv_results_dict['shots_off_target'])
        results_free_kicks_str="Free Kicks -   For: {}   Against: {}".format(self.csv_results_dict['free_kicks_for'], self.csv_results_dict['free_kicks_against'])
        results_goals_str="Goals -   For: {}   Against: {}".format(self.csv_results_dict['goals_for'], self.csv_results_dict['goals_against'])
        
        # team, date and KO time widgets
        results_teams_str_label=tk.Label(self.frame1a_sports_finished, text=results_teams_str)
        results_teams_str_label.grid(row=3, column=1, columnspan=3, padx=1, pady=1)
        results_date_str_label=tk.Label(self.frame1a_sports_finished, text=results_date_str)
        results_date_str_label.grid(row=4, column=1, columnspan=3)
        results_ko_time_label=tk.Label(self.frame1a_sports_finished, text=results_ko_time_str)
        results_ko_time_label.grid(row=5, column=1, columnspan=3)
        
        # add separator - just to demarcate macro data and 
        separator_4=ttk.Separator(self.frame1a_sports_finished, orient='horizontal')
        separator_4.grid(row=6, column=0, columnspan=4, padx=20, pady=20, sticky='w, n, e, s')
        
        # shots, free kicks and goal widgets
        results_shots_str_label=tk.Label(self.frame1a_sports_finished, text=results_shots_str)
        results_shots_str_label.grid(row=7, column=1, columnspan=3)
        results_free_kicks_str_label=tk.Label(self.frame1a_sports_finished, text=results_free_kicks_str)
        results_free_kicks_str_label.grid(row=8, column=1, columnspan=3)
        results_goals_str_label=tk.Label(self.frame1a_sports_finished, text=results_goals_str)
        results_goals_str_label.grid(row=9, column=1, columnspan=3)
        
                
        # create a Close button and place it using grid()
        results_frame1a_close_button=tk.Button(self.frame1a_sports_finished,text="Close", padx=5, pady=5, underline=True, background='white', command=self.close_button_click)
        results_frame1a_close_button.grid(row=11, column=1, padx=10, pady=5, columnspan=3, sticky='w n e s')
        
        # #resizing second frame config using grid weights 
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.frame1a_sports_finished.columnconfigure(0, weight=3)
        self.frame1a_sports_finished.columnconfigure(1, weight=3)
        self.frame1a_sports_finished.columnconfigure(2, weight=3)
        self.frame1a_sports_finished.columnconfigure(3, weight=3)
        self.frame1a_sports_finished.columnconfigure(4, weight=3)
        self.frame1a_sports_finished.rowconfigure(0, weight=3)
        self.frame1a_sports_finished.rowconfigure(1, weight=3)
        self.frame1a_sports_finished.rowconfigure(2, weight=3)
        self.frame1a_sports_finished.rowconfigure(3, weight=3)
        self.frame1a_sports_finished.rowconfigure(4, weight=3)
        self.frame1a_sports_finished.rowconfigure(5, weight=3)
        self.frame1a_sports_finished.rowconfigure(6, weight=3)
        self.frame1a_sports_finished.rowconfigure(7, weight=3)
        self.frame1a_sports_finished.rowconfigure(8, weight=3)
        self.frame1a_sports_finished.rowconfigure(9, weight=3)

    
    # when click finish button we need to write all the data to the earlier created csv file
    # we will then read the last row and headers from the csv file and store that data in s dictionary in key value pairs
    # then get rid of old frame and call a new frame which will display the stats
    # finishes by calling the previous function sports_replace_frame()
    def finish_button_click(self):
        # get data from widgets using the .get method to return the current value of the widget and store them as variables
        date=self.sports_day_combo.get()
        month=self.sports_month_combo.get()
        year=self.sports_year_combo.get()
        ko_time=self.sports_time_combo.get()
        home_team=self.sports_home_team_entry.get()
        away_team=self.sports_away_team_entry.get()
        
        # write data to csv file
        # we use 'with' statement so we don't have to close the file afterwards
        with open(self.csv_file_name_and_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date, month, year, ko_time, home_team, away_team, self.shots_on_target_intvar.get(), self.shots_off_target_intvar.get(), self.free_kicks_for_intvar.get(), self.free_kicks_against_intvar.get(), self.goals_for_intvar.get(), self.goals_against_intvar.get()
                            ])

        self.sports_replace_frame()




    def realtime_intvar_values(self):
        # create widgets to display realtime intvar() values, so user knows it is working and 
        # can see in realtime what the values are
        self.sports_sont_intvar_current_value_label=tk.Label(self.frame1_sports, textvariable=self.sports_sont_string_and_realtime_intvar)
        self.sports_sont_intvar_current_value_label.grid(row=10, column=0, sticky='e')
        self.sports_sofft_intvar_current_value_label=tk.Label(self.frame1_sports, textvariable=self.sports_sofft_string_and_realtime_intvar)
        self.sports_sofft_intvar_current_value_label.grid(row=10, column=2, sticky='e')
        self.sports_fkf_intvar_current_value_label=tk.Label(self.frame1_sports, textvariable=self.sports_fkf_string_and_realtime_intvar)
        self.sports_fkf_intvar_current_value_label.grid(row=12, column=0, sticky='e')
        self.sports_fka_intvar_current_value_label=tk.Label(self.frame1_sports, textvariable=self.sports_fka_string_and_realtime_intvar)
        self.sports_fka_intvar_current_value_label.grid(row=12, column=2, sticky='e')
        self.sports_gf_intvar_current_value_label=tk.Label(self.frame1_sports, textvariable=self.sports_gf_string_and_realtime_intvar)
        self.sports_gf_intvar_current_value_label.grid(row=14, column=0, sticky='e')
        self.sports_ga_intvar_current_value_label=tk.Label(self.frame1_sports, textvariable=self.sports_ga_string_and_realtime_intvar)
        self.sports_ga_intvar_current_value_label.grid(row=14, column=2, sticky='e')
    

    def user_guide_button_click(self):
        # 
        self.user_guide_file_path=os.path.dirname(os.path.realpath(__file__))
        # define csv file name to store data. could prompt user for its name and define outside of function but it is not used, seen or interacted with user in the app so just lf it hard coded here 
        self.user_guide_file_name="user_guide.txt"
        self.user_guide_file_name_and_path=os.path.join(self.user_guide_file_path, self.user_guide_file_name)

        # create new window, which is still a child of 'root', a new separate window
        user_guide_window=tk.Toplevel(self.root)
        user_guide_window.title("User Guide")
        user_guide_window.geometry('600x400')
        
        # open the user_guie.txt, read contents and assign to a variable
        with open(self.user_guide_file_name_and_path, 'r') as file:
            user_guide_text_content=file.read()
            
        user_guide_text_obj=tk.Text(user_guide_window, wrap="word")
        user_guide_text_obj.insert('1.0', user_guide_text_content)
        user_guide_text_obj.configure(state='disabled')
        user_guide_text_obj.pack(fill='both', expand=True)
        
        
    def close_button_click(self):
        self.root.quit()
        self.root.destroy()
        

    # Start the Tkinter event loop
    def start_match_analysis_app(self):
        self.root.mainloop()
