import os # used for filer and path work
from pathlib import Path
#
# user_guide_file_path=os.path.dirname(os.path.realpath(__file__))

# filename="user_guide.txt"
# # user_guide_file_path=os.path.realpath(filename)

# user_guide_file_path=Path(filename).resolve()


# print(user_guide_file_path)

user_guide_file_path=os.path.dirname(os.path.realpath(__file__))
        # define csv file name to store data. could prompt user for its name and define outside of function but it is not used, seen or interacted with user in the app so just lf it hard coded here 
user_guide_file_name="user_guide.txt"
user_guide_file_name_and_path=os.path.join(user_guide_file_path, user_guide_file_name)
print(user_guide_file_name_and_path)