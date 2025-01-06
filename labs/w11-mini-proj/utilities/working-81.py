import os
import csv

        # list of headers we will use and track data for in csv file from app usage.hard coded here as no user interaction with the file
        # and keeps it all self contained
        
py_file_location=os.path.dirname(os.path.realpath(__file__))
        # define csv file name to store data. could prompt user for its name but there is more scopefor errorin not picking up the right file, r in the app so just lf filename here 
csv_speed_file_name="travel_mode_speeds.csv"
csv_speed_file_name_and_path=os.path.join(py_file_location, csv_speed_file_name)
csv_distances_file_name="planet_distances.csv"
csv_distances_file_name_and_path=os.path.join(py_file_location, csv_distances_file_name)

        # create dictionaries to store  csv data
#speed_dict={}
#distances_dict={}
        
        # open speed csv, read its contents into dictionary.
with open(csv_speed_file_name_and_path, 'r', newline='') as file:
    speed_reader=list(csv.reader(file))
    for row in speed_reader:
        speed_headers=speed_reader[0]
        speed_last_row=speed_reader[-1]

#create dictionary by zipping two lists together
speed_dict=dict(zip(speed_headers, speed_last_row))
print(speed_dict)
        
#open distance csv, read its contents and split into two lists 
with open(csv_distances_file_name_and_path, 'r', newline='') as file:
    dist_reader=list(csv.reader(file))
    for row in dist_reader:
        dist_headers=dist_reader[0]
        dist_last_row=dist_reader[-1]

#create distances dictionary by zipping two lists together
distance_dict=dict(zip(dist_headers, dist_last_row))
print(distance_dict)  

# create time dictionary
time_dict={}

# iterate through speed and distance dictionarys to calculate time taken values
for mode, speed in speed_dict.items():
    time_dict[mode] = {}
    for planet, distance in distance_dict.items():
        time_dict[mode][planet] = int(distance)/int(speed)


print(time_dict)

cycle_mercury_time = time_dict['cycle']['Mercury']
print(f"Time for cycle to Mercury: {cycle_mercury_time} hours")

rocket_mars_time = time_dict['rocket']['Mars']
print(f"Time to take a rocket to mars: {rocket_mars_time} hours")