import tkinter as tk # used for tk works
from tkinter import ttk # some ttk widgets used
import os

class FileNotExist(Exception):
    pass

class Gravity:
    
    def __init__(self):
        
        self.root = tk.Tk()
        self.root.title("Mini project - 3 applications - Jan 2025")
             
        # Create frame , header and description and place them into the root window using grid()
        self.gravity_frame = tk.Frame(self.root, borderwidth=2, relief="groove", padx=5, pady=10)
        self.gravity_frame.grid(row=0, column=0, padx=10, pady=10, sticky=('N', 'W', 'E', 'S'))
        
        self.gravity_frame_header = tk.Label(self.gravity_frame, text="Gravitational Pull ", font=("Helvetica", 10, "bold"))
        self.gravity_frame_header.grid(row=0, column=0, columnspan=3, padx=1, pady=5, sticky="w")
        
        self.gravity_frame_desc = ttk.Label(self.gravity_frame, text="Calculate the Gravitational pull between two objects", font=("Helvetica", 8, "normal"))
        self.gravity_frame_desc.grid(row=1, column=0, columnspan=3, padx=1, pady=1, sticky="w, n")
        
        # add separator - just to demarcate different areas of gui
        separator_1=ttk.Separator(self.gravity_frame, orient='horizontal')
        separator_1.grid(row=2, column=0, columnspan=5, padx=20, pady=20, sticky='w, n, e, s')
        
        self.create_gravity_widgets()
        

    def create_gravity_widgets(self):
        
        # create app widgets for each planet to go into frame
        # create widget objects for home team and away team data
        self.obj1_gravity_label= ttk.Label(self.gravity_frame, text='Object 1 Name:')
        self.obj1_gravity_label.grid(row=3, column=0, sticky='W')
        self.obj1_gravity_name = tk.StringVar(value='none')
        self.obj1_gravity_name_entry= ttk.Entry(self.gravity_frame, textvariable=self.obj1_gravity_name)
        self.obj1_gravity_name_entry.grid(row=4, column=0, padx=2, pady=2, columnspan=1, sticky='w')

        self.mass1_gravity_label= ttk.Label(self.gravity_frame, text='Mass (Kgs):')
        self.mass1_gravity_label.grid(row=3, column=1, sticky='W')
        self.mass1_gravity = tk.IntVar(value=0)
        self.mass1_gravity_name_entry= ttk.Entry(self.gravity_frame, textvariable=self.mass1_gravity)
        self.mass1_gravity_name_entry.grid(row=4, column=1, padx=2, pady=2, columnspan=1, sticky='w')


        separator_1=ttk.Separator(self.gravity_frame, orient='vertical')
        separator_1.grid(row=3, column=0, rowspan=3, padx=10, pady=10, sticky='e')

        self.obj2_gravity_label= ttk.Label(self.gravity_frame, text='Object 2 Name:')
        self.obj2_gravity_label.grid(row=3, column=3, sticky='e')
        self.obj2_gravity_name = tk.StringVar(value='none')
        self.obj2_gravity_entry= ttk.Entry(self.gravity_frame, textvariable=self.obj2_gravity_name)
        self.obj2_gravity_entry.grid(row=4, column=3, padx=2, pady=2, columnspan=1, sticky='e')
        
        self.mass2_gravity_label= ttk.Label(self.gravity_frame, text='Mass (Kgs):')
        self.mass2_gravity_label.grid(row=3, column=4, sticky='e')
        self.mass2_gravity = tk.IntVar(value=0)
        self.mass2_gravity_name_entry= ttk.Entry(self.gravity_frame, textvariable=self.mass2_gravity)
        self.mass2_gravity_name_entry.grid(row=4, column=4, padx=2, pady=2, columnspan=1, sticky='e')
        
        self.distance_gravity_label= ttk.Label(self.gravity_frame, text='Distance between Objects (mtrs)')
        self.distance_gravity_label.grid(row=5, column=2, sticky='e')
        self.distance_gravity = tk.IntVar(value=0)
        self.distance_gravity_name_entry= ttk.Entry(self.gravity_frame, textvariable=self.distance_gravity)
        self.distance_gravity_name_entry.grid(row=6, column=2, padx=2, pady=2, columnspan=1, sticky='w, e')
        
        
        self.mass_distance_msg_label= ttk.Label(self.gravity_frame, text='Note: The values entered for mass and distance must be whole number integers. Mass values should be entered in Kgs and distances in mtrs:')
        self.mass_distance_msg_label.grid(row=7, column=0, columnspan=4, sticky='w, e')
        
        
        separator_2=ttk.Separator(self.gravity_frame, orient='horizontal')
        separator_2.grid(row=8, column=0, columnspan=5, padx=10, pady=10, sticky='w, n, e, s')


        #re-sizing
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.gravity_frame.columnconfigure(0, weight=3)
        self.gravity_frame.columnconfigure(1, weight=3)
        self.gravity_frame.columnconfigure(2, weight=3)
        self.gravity_frame.columnconfigure(3, weight=3)
        self.gravity_frame.columnconfigure(4, weight=3)
        self.gravity_frame.rowconfigure(0, weight=3)
        self.gravity_frame.rowconfigure(1, weight=3)
        self.gravity_frame.rowconfigure(2, weight=3)
        self.gravity_frame.rowconfigure(3, weight=3)
        self.gravity_frame.rowconfigure(4, weight=3)
        self.gravity_frame.rowconfigure(5, weight=3)
        self.gravity_frame.rowconfigure(6, weight=3)
        self.gravity_frame.rowconfigure(7, weight=3)
        self.gravity_frame.rowconfigure(8, weight=3)
        self.gravity_frame.rowconfigure(9, weight=3)
        self.gravity_frame.rowconfigure(10, weight=3)
        self.gravity_frame.rowconfigure(11, weight=3)
        self.gravity_frame.rowconfigure(12, weight=3)
        self.gravity_frame.rowconfigure(13, weight=3)
        self.gravity_frame.rowconfigure(14, weight=3)   


        self.create_calculate_userguide_buttons()
        
        
    def create_calculate_userguide_buttons(self):
        
        calculate_button=tk.Button(self.gravity_frame ,text="Calculate", padx=5, pady=5, underline=True, background='white', command=self.calculate_button_click)
        calculate_button.grid(row=9, column=0, padx=10, pady=5, sticky='e')
        
        # create User Guide button and place it using grid()
        gravity_user_guide_button=tk.Button(self.gravity_frame, text="User Guide", padx=5, pady=5, underline=True, background='white', command=self.user_guide_button_click)
        gravity_user_guide_button.grid(row=9, column=4, padx=10, pady=5, sticky='w')
        
        # add separator - just to demarcate different areas of gui
        separator_3=ttk.Separator(self.gravity_frame, orient='horizontal')
        separator_3.grid(row=10, column=0, columnspan=5, padx=20, pady=20, sticky='w, n, e, s')
        
    
    def calculate_button_click(self):  
    
        self.obj1_name=self.obj1_gravity_name.get()
        self.obj2_name=self.obj2_gravity_name.get()
        
        if not self.obj1_name or not self.obj2_name:
            raise ValueError('Object names cannot be empty')
        
        self.obj1_mass=float(self.mass1_gravity.get())
        self.obj2_mass=float(self.mass2_gravity.get())
        self.dist_between_objs=float(self.distance_gravity.get())
        
        if not self.obj1_mass or not self.obj2_mass or not self.dist_between_objs:
            raise ValueError('Mass and distance values cannot be empty')
        
        print(self.obj1_name)
        print(self.obj2_name)
        print(self.obj1_mass)
        print(self.obj2_mass)
        print(self.dist_between_objs)
        
        
        if self.dist_between_objs == 0:
            dist_zero_msg_label=tk.Label(self.gravity_frame, text='Distance cannot be zero, please re-launch the application, enter a valid value and trey again. The application will now exit')
            dist_zero_msg_label.grid(row=11, column=1, columnspan=3, padx=5, pady=5, sticky='w')
            
        

        # The value of the Gravitational constant is approximately 6.674 × 10-11 m3 kg-1 s-2.
        # gravitational_constant
        G=6.674*10**-11
        
        #calculate gravitational pull
        gforce=G*(self.obj1_mass*self.obj2_mass)/(self.dist_between_objs**2)
        
        print(gforce)
        
        display_gforce_label=tk.Label(self.gravity_frame, text='Gravitational force between the \'{}\' and \'{}\' is \'{}\' Newtons: '.format(self.obj1_name, self.obj2_name, gforce))
        display_gforce_label.grid(row=11, column=1, columnspan=4, padx=5, pady=5, sticky='w')
        
       
        # create a Close button and place it using grid()
        gravity_close_button=tk.Button(self.gravity_frame, text="Close", padx=5, pady=5, underline=True, background='white', command=self.close_button_click)
        gravity_close_button.grid(row=20, column=1, columnspan=2, padx=10, pady=5, sticky='w n e s')
    
    
    def user_guide_button_click(self):
        
        self.user_guide_file_path=os.path.dirname(os.path.realpath(__file__))
        # define csv file name to store data. could prompt user for its name and define outside of function but it is not used, seen or interacted with user in the app so just lf it hard coded here 
        self.user_guide_file_name="user_guide_gravity.txt"
        self.user_guide_file_name_and_path=os.path.join(self.user_guide_file_path, self.user_guide_file_name)
        


        # create new window, which is still a child of 'root', a new separate window
        user_guide_window=tk.Toplevel(self.root)
        user_guide_window.title("User Guide")
        user_guide_window.geometry('600x400')
        
        try:

            # open the user_guise.txt, read contents and assign to a variable
            with open(self.user_guide_file_name_and_path, 'r') as file:
                user_guide_text_content=file.read()
        
        except FileNotExist as fne1:
            print("-->> user guide file not exist exception catch - fne1")
            
        user_guide_text_obj=tk.Text(user_guide_window, wrap="word")
        user_guide_text_obj.insert('1.0', user_guide_text_content)
        user_guide_text_obj.configure(state='disabled')
        user_guide_text_obj.pack(fill='both', expand=True)
    
    def close_button_click(self):
        # this stops the event loop
        self.root.quit()
        # this destroys the root window gui
        self.root.destroy()
        
    
    def start_gravity_app(self):
        self.root.mainloop()