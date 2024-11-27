# Week 2 - Ex 2 - cutting the grass

# Prompt user to input their full name with space between them
full_name_str=input("Please enter your name and surname with a space typed between them: ")

# convert string to lower case to standardize the input to all lower case
full_name_str.lower()

# convert string object type to list object type
full_name_list=full_name_str.split()

# define a new string object that takes the elements in the list object and capitalises them
# calling the second list item first, and the first letter in the first list item second
display_name=(full_name_list[1].capitalize() + ", " + full_name_list[0][0].capitalize())

# print the new string object
print(display_name)



