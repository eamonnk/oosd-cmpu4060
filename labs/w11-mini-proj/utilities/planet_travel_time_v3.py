import tkinter as tk # used for tk works
from tkinter import ttk # some ttk widgets used
import os # used for filer and path work
import csv # needed for csv file data which we will use as our data source

# https://theplanets.org/distances-between-planets/

class FileNotExist(Exception):
    pass

class PlanetTravelTime:
    
    def __init__(self):
    
        try:
            self.root = tk.Tk()
            self.root.title("Mini project - 3 applications - Jan 2025")
            
            # Create frame , header and description and place them into the root window using grid()
            self.planet_frame = tk.Frame(self.root, borderwidth=2, relief="groove", padx=5, pady=10)
            self.planet_frame.grid(row=0, column=0, padx=10, pady=10, sticky=('N', 'W', 'E', 'S'))
            
            self.planet_frame_header = tk.Label(self.planet_frame, text="Planet Travel Time ", font=("Helvetica", 10, "bold"))
            self.planet_frame_header.grid(row=0, column=0, columnspan=3, padx=1, pady=5, sticky="w")
            
            self.planet_frame_desc = ttk.Label(self.planet_frame, text="Calculate travel time from Earth to different planets using different means of transport", font=("Helvetica", 8, "normal"))
            self.planet_frame_desc.grid(row=1, column=0, columnspan=3, padx=1, pady=1, sticky="w, n")
            
            # add separator - just to demarcate different areas of gui
            separator_1=ttk.Separator(self.planet_frame, orient='horizontal')
            separator_1.grid(row=2, column=0, columnspan=4, padx=20, pady=20, sticky='w, n, e, s')
            
            self.create_planet_and_transport_widgets()

        except InitException as inite1:
            print("-->> initialization exception in match analysis")
        
    def create_planet_and_transport_widgets(self):
        
        #create variable to hold planet selection value
        self.chosen_planet=tk.StringVar(value='none')
        
        # create app radio button planet widgets for each planet to go into frame
        radio_button_sun=tk.Radiobutton(self.planet_frame, text='Sun', variable=self.chosen_planet, value='sun')
        radio_button_sun.grid(row=3, column=0, padx=5, pady=5, sticky='w')
    
        radio_button_mercury=tk.Radiobutton(self.planet_frame, text='Mercury', variable=self.chosen_planet, value='mercury')
        radio_button_mercury.grid(row=4, column=0, padx=5, pady=5, sticky='w')
        
        radio_button_venus=tk.Radiobutton(self.planet_frame, text='Venus', variable=self.chosen_planet, value='venus')
        radio_button_venus.grid(row=5, column=0, padx=5, pady=5, sticky='w')
        
        radio_button_mars=tk.Radiobutton(self.planet_frame, text='Mars', variable=self.chosen_planet, value='mars')
        radio_button_mars.grid(row=6, column=0, padx=5, pady=5, sticky='w')
        
        radio_button_jupiter=tk.Radiobutton(self.planet_frame, text='Jupiter', variable=self.chosen_planet, value='jupiter')
        radio_button_jupiter.grid(row=7, column=0, padx=5, pady=5, sticky='w')
        
        radio_button_saturn=tk.Radiobutton(self.planet_frame, text='Saturn', variable=self.chosen_planet, value='saturn')
        radio_button_saturn.grid(row=8, column=0, padx=5, pady=5, sticky='w')
        
        radio_button_uranus=tk.Radiobutton(self.planet_frame, text='Uranus', variable=self.chosen_planet, value='uranus')
        radio_button_uranus.grid(row=9, column=0, padx=5, pady=5, sticky='w')
        
        radio_button_neptune=tk.Radiobutton(self.planet_frame, text='Neptune', variable=self.chosen_planet, value='neptune')
        radio_button_neptune.grid(row=10, column=0, padx=5, pady=5, sticky='w')
        
        radio_button_pluto=tk.Radiobutton(self.planet_frame, text='Pluto', variable=self.chosen_planet, value='pluto')
        radio_button_pluto.grid(row=11, column=0, padx=5, pady=5, sticky='w')
        
        # create variable to hold travel mode value
        self.chosen_travel_mode=tk.StringVar(value='none')
        
        # create mode of travel widgets 
        radio_button_walk=tk.Radiobutton(self.planet_frame, text='Walk', variable=self.chosen_travel_mode, value='walk')
        radio_button_walk.grid(row=3, column=2, padx=5, pady=5, sticky='w')
        
        radio_button_run=tk.Radiobutton(self.planet_frame, text='Run', variable=self.chosen_travel_mode, value='run')
        radio_button_run.grid(row=4, column=2, padx=5, pady=5, sticky='w')
        
        radio_button_cycle=tk.Radiobutton(self.planet_frame, text='Cycle', variable=self.chosen_travel_mode, value='cycle')
        radio_button_cycle.grid(row=5, column=2, padx=5, pady=5, sticky='w')
        
        radio_button_drive=tk.Radiobutton(self.planet_frame, text='Drive', variable=self.chosen_travel_mode, value='drive')
        radio_button_drive.grid(row=6, column=2, padx=5, pady=5, sticky='w')
        
        radio_button_airplane=tk.Radiobutton(self.planet_frame, text='Airplane', variable=self.chosen_travel_mode, value='airplane')
        radio_button_airplane.grid(row=7, column=2, padx=5, pady=5, sticky='w')
        
        radio_button_rocket=tk.Radiobutton(self.planet_frame, text='Rocket', variable=self.chosen_travel_mode, value='rocket')
        radio_button_rocket.grid(row=8, column=2, padx=5, pady=5, sticky='w')
        
        radio_button_speedoflight=tk.Radiobutton(self.planet_frame, text='Speed of Light', variable=self.chosen_travel_mode, value='speed_of_light')
        radio_button_speedoflight.grid(row=9, column=2, padx=5, pady=5, sticky='w')
        
        
        # add separator - just to demarcate different areas of gui
        separator_2=ttk.Separator(self.planet_frame, orient='horizontal')
        separator_2.grid(row=12, column=0, columnspan=4, padx=20, pady=20, sticky='w, n, e, s')
        
        #re-sizing
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.planet_frame.columnconfigure(0, weight=3)
        self.planet_frame.columnconfigure(1, weight=3)
        self.planet_frame.columnconfigure(2, weight=3)
        self.planet_frame.columnconfigure(3, weight=3)
        self.planet_frame.columnconfigure(4, weight=3)
        self.planet_frame.rowconfigure(0, weight=3)
        self.planet_frame.rowconfigure(1, weight=3)
        self.planet_frame.rowconfigure(2, weight=3)
        self.planet_frame.rowconfigure(3, weight=3)
        self.planet_frame.rowconfigure(4, weight=3)
        self.planet_frame.rowconfigure(5, weight=3)
        self.planet_frame.rowconfigure(6, weight=3)
        self.planet_frame.rowconfigure(7, weight=3)
        self.planet_frame.rowconfigure(8, weight=3)
        self.planet_frame.rowconfigure(9, weight=3)
        self.planet_frame.rowconfigure(10, weight=3)
        self.planet_frame.rowconfigure(11, weight=3)
        self.planet_frame.rowconfigure(12, weight=3)
        self.planet_frame.rowconfigure(13, weight=3)
        self.planet_frame.rowconfigure(14, weight=3)    
        
        
        self.create_calculate_userguide_button()
        self.create_datasets()
        
    def create_calculate_userguide_button(self):
        
        calculate_button=tk.Button(self.planet_frame ,text="Calculate", padx=5, pady=5, underline=True, background='white', command=self.calculate_button_click)
        calculate_button.grid(row=13, column=0, padx=10, pady=5, sticky='e')
        
        # create User Guide button and place it using grid()
        planet_user_guide_button=tk.Button(self.planet_frame,text="User Guide", padx=5, pady=5, underline=True, background='white', command=self.user_guide_button_click)
        planet_user_guide_button.grid(row=13, column=2, padx=10, pady=5, sticky='w')
        
        # add separator - just to demarcate different areas of gui
        separator_3=ttk.Separator(self.planet_frame, orient='horizontal')
        separator_3.grid(row=14, column=0, columnspan=4, padx=20, pady=20, sticky='w, n, e, s')

    # create data sets from external csv data sources from which we can subsequently calculate the values we need 
    
    def create_datasets(self):
        # have 2 csv files:
        # 1. containing distances from earth to the planet
        # 2. speeds for different modes of transport
        # Both need to be placed alongside this .py file, in the same directory.
        # , used some references below to make sure it gets created 
        # in same location as current .py file
        # https://docs.python.org/3/library/os.path.html ++ https://sqlpey.com/python/top-10-methods-to-retrieve-full-path/
        
        try:
            self.py_file_location=os.path.dirname(os.path.realpath(__file__))
            # define csv file name to store data. could prompt user for its name but there is more scopefor errorin not picking up the right file, r in the app so just lf filename here 
            self.csv_speed_file_name="travel_mode_speeds.csv"
            self.csv_speed_file_name_and_path=os.path.join(self.py_file_location, self.csv_speed_file_name)
            self.csv_distances_file_name="planet_distances.csv"
            self.csv_distances_file_name_and_path=os.path.join(self.py_file_location, self.csv_distances_file_name)

            # open speed csv, read its contents and split into two lists 
            with open(self.csv_speed_file_name_and_path, 'r', newline='') as file:
                speed_reader=list(csv.reader(file))
                for row in speed_reader:
                    speed_headers=speed_reader[0]
                    speed_last_row=speed_reader[-1]

        except FileNotExist as csvne1:
            print("-->> csv file not exist exception catch - csvne1")
        
        #create speed dictionary by zipping two lists together
        self.speed_dict=dict(zip(speed_headers, speed_last_row))
        print(self.speed_dict)   
        
        try:
            #open distance csv, read its contents and split into two lists 
            with open(self.csv_distances_file_name_and_path, 'r', newline='') as file:
                dist_reader=list(csv.reader(file))
                for row in dist_reader:
                    dist_headers=dist_reader[0]
                    dist_last_row=dist_reader[-1]

        except FileNotExist as fne2:
            print("-->> file not exist exception catch - fne1")

        #create distances dictionary by zipping two lists together
        self.distance_dict=dict(zip(dist_headers, dist_last_row))
        print(self.distance_dict)  
        
        self.create_time_data()
    
        # create dictionary of time values based on distance and speed data we created in previous function
        # time values are based on the formula Time =  Distance/ Speed
        # we will create a nested dictionary to store the calculated values which we will then call at run time
        # which will be more efficient then calculating a value each time calculate button is clicked
    def create_time_data(self):
        
        # create time dictionary
        self.time_dict={}
        
        # iterate through speed and distance dictionarys to calculate time taken values
        # we will create  a sub-dictionary for each mode of travel i.e. bike, cycle, car etc
        # distance = Kms 
        # speed = KM/Hr
        # => Time =Distance / Speed and is in Hours by default
        for mode, speed in self.speed_dict.items():
            self.time_dict[mode] = {}
            for planet, distance in self.distance_dict.items():
                self.time_dict[mode][planet] = round(int(distance)/int(speed), 2)
                
    
        print(self.time_dict)
    
    
    def calculate_button_click(self):
        
        #self.create_results_widgets()
        
        selected_planet=self.chosen_planet.get()
        selected_travel=self.chosen_travel_mode.get()
        
        if selected_planet == 'none' or selected_travel == 'none':
            result_time="please select both a planet and travel mode and try again."
        else:
            result_time = self.time_dict[selected_travel][selected_planet]
        
        # print(selected_planet)
        # print(selected_travel)
        
        print("Travel time via {} from Earth to {} is {} hours :".format(selected_travel, selected_planet, result_time))
        
        result_label=tk.Label(self.planet_frame, text="Travel time via {} from Earth to {} is:".format(selected_travel, selected_planet))
        result_label.grid(row=16, column=0, columnspan=3, padx=3, pady=3, sticky='w, n, e, s')
        
        result_label=tk.Label(self.planet_frame, text=" {} hours: ".format(result_time))
        result_label.grid(row=17, column=0, columnspan=3, padx=3, pady=3, sticky='w, n, e, s')
        result_label=tk.Label(self.planet_frame, text=" {} Days: ".format(round(result_time/24), 0))
        result_label.grid(row=18, column=0, columnspan=3, padx=3, pady=3, sticky='w, n, e, s')
        result_label=tk.Label(self.planet_frame, text=" {} Years: ".format(round((result_time/24)/365.25), 0))
        result_label.grid(row=19, column=0, columnspan=3, padx=3, pady=3, sticky='w, n, e, s')
        
    
        # create a Close button and place it using grid()
        planet_close_button=tk.Button(self.planet_frame, text="Close", padx=5, pady=5, underline=True, background='white', command=self.close_button_click)
        planet_close_button.grid(row=20, column=1, padx=10, pady=5, sticky='w n e s')
    
    def user_guide_button_click(self):
        # 
        self.user_guide_file_path=os.path.dirname(os.path.realpath(__file__))
        # define csv file name to store data. could prompt user for its name and define outside of function but it is not used, seen or interacted with user in the app so just lf it hard coded here 
        self.user_guide_file_name="user_guide_planet.txt"
        self.user_guide_file_name_and_path=os.path.join(self.user_guide_file_path, self.user_guide_file_name)
        


        # create new window, which is still a child of 'root', a new separate window
        user_guide_window=tk.Toplevel(self.root)
        user_guide_window.title("User Guide")
        user_guide_window.geometry('600x400')
        
        try:

            # open the user_guie.txt, read contents and assign to a variable
            with open(self.user_guide_file_name_and_path, 'r') as file:
                user_guide_text_content=file.read()
        
        except FileNotExist as fne3:
            print("-->> user guide file not exist exception catch - fne3")
            
        user_guide_text_obj=tk.Text(user_guide_window, wrap="word")
        user_guide_text_obj.insert('1.0', user_guide_text_content)
        user_guide_text_obj.configure(state='disabled')
        user_guide_text_obj.pack(fill='both', expand=True)
    
    def close_button_click(self):
        # this stops the event loop
        self.root.quit()
        # this destroys the root window gui
        self.root.destroy()
        
    
    def start_planet_travel_time_app(self):
        self.root.mainloop()