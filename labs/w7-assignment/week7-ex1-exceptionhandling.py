'''
Week 7 Assignment - Exception handling

--exception-handling-1.py--
-eamonn kelly
'''

# value for number rof items, as per spec
REQ_LIST_LEN = 5

# flag to track number of attempts to enter correct data. Used in while loop below.
num_tries_1=0

# Prompt user to input their full name with space between them
# while loop to give the user 2 goes to enter correct data

# adding try excep construct to catch any errors
try:

    while num_tries_1 < 2:

        # take in user data  for items and split it to a list, it comes in as a str, so we convert immediately for efficiency
        user_items_list=(input("\nPlease enter a list of {} items to be rated, separated by spaces: ".format(REQ_LIST_LEN))).split()
        
        # check if number of items entered matches our required value. If not print a msg telling user, increment try value and go again.
        if (len(user_items_list)) != REQ_LIST_LEN:
            print("\n You have not entered the correct number of items. \n You should enter {} seperate items and all items should be text based. Please Try Again.".format(REQ_LIST_LEN ))
            num_tries_1 += 1
            continue

        # Checking if characters are alphabet. IsDigit only works on full str not if numbers are embedded in str. So 
        # need to modify check to check if all alpha and then verify against entered list. If both are equal all characters are alphabet.
        # we use lambda exp to filter list for alpha characters and put i a list, then compare lists and if True enter loop 
        # and notify user not all strings in entered list are alpha
        
        is_alpha_check = list(filter(lambda item: item.isalpha(), user_items_list))
        if user_items_list != is_alpha_check:
            print("\nYou have entered numbers. You need to enter text based items. Please Try Again.")
            num_tries_1 += 1
            continue
        
        # if neither condition met, data is deemed valid and continue on to rest of program
        print ("You have entered valid items")
        break

    if num_tries_1 == 2:
        print("\nYou have entered in valid items twice. The program is exiting. You may re run the program to try again. \nThank You.")
        exit()

# closing try-except construct, have variable ve1 to hold any exception object data
except ValueError as ve1:
    print("ValueError: A non number value was detected. Please check all inputted numbers are numbers")
    print("Exception message:", ve1)

indexed_items=list(enumerate(user_items_list, start=1))
for index, item in indexed_items:
        print("{} {}".format(index, item))


# create valid range list and couldn't get it to work off range method itself... so put in a list. 
# List if Ints tho, and user pref list if str, so had to convert this 'int' list to 'str' list so can compare 
# for conditional error handling

# adding try statement to catch errors, have except below to print a statement if error encountered 
# and a variable to hold the excpetion
try:
    # set try count value for while loop
    num_tries_2=0

    # create a list of numbers based on range criteria and variable defined st start, start, stop and step values.
    valid_list_range=list((range(1, REQ_LIST_LEN+1, 1)))

    # convert list to str so can compare against user pref list for conditional error handling
    valid_list_range_str = [str(item) for item in valid_list_range]


    # loop to check valid numbers in range by comparing user pref to range list and len of user pref numbers
    # users get two chances then program exist with msg
    while num_tries_2 < 2:
        user_pref=input("User > Please enter the item ids in order of your preference for the items, separated by spaces: ").split()
    # conditions for len and valid numbers:
        if sorted(valid_list_range_str) != sorted(user_pref) or len(valid_list_range_str) != len(user_pref):
            print("User - You have entered values not in range or too many numbers. You must enter numbers between 1 and {}. ".format(REQ_LIST_LEN))
            num_tries_2 += 1
            continue
        else:
            print("You have entered valid preferences")
            break

        
    if num_tries_2 == 2:
        print("\nYou have entered in valid items twice. The program is exiting. You may re-run the program to try again. \nThank You.")
        exit()
# closing the try - except construct, added ie as variable to hold any exception object
except IndexError as ie:
    print("Index Error: Tried to access an element in a list using an index that is out of range")
    print("Exception message:", ie)

# conditional error handling for friend values
# Tried to do for both at same time using zip function, but couldn't get ti to work, so hasd to split it out, resulting in some duplication ion code
# set try count value for while loop
num_tries_3=0

# did not add try except construct, left it with conditional error handling
# loop to check valid numbers in range by comparing user pref to range list and len of user pref numbers
# users get two chances then program exist with msg
while num_tries_3 < 2:
    frnd_pref=input("Friend > Please enter the item ids in order of your preference for the items, separated by spaces: ").split()
# conditions for len and valid numbers:
    if sorted(valid_list_range_str) != sorted(frnd_pref) or len(valid_list_range_str) != len(frnd_pref):
        print("User - You have entered values not in range or too many numbers. You must enter numbers between 1 and {}. ".format(REQ_LIST_LEN))
        num_tries_2 += 1
        continue
    else:
        print("You have entered valid preferences")
        break

if num_tries_2 == 2:
    print("\nYou have entered in valid items twice. The program is exiting. You may re-run the program to try again. \nThank You.")
    exit()


#add try statement to try catch any potential errors
try:
# two lists one sorted based on order of the other. Using lambda function, specifyin int as valeu is a str in list
# using .join to get rid of parenthesis and specifcy separator.
#ordered_list = sorted(indexed_items, key=lambda item: user_pref.index(item[0]))
    ordered_user_list = (list(map(lambda pref: user_items_list[int(pref) -1], user_pref)))
    ordered_frnd_list = (list(map(lambda pref: user_items_list[int(pref) -1], frnd_pref)))


# For loop to print two user list preferences. we use a for loop over the two lists with string identifiers, build a statement using join and then print the statemnent

    for user_type, user_list in [("User", ordered_user_list), ("Friend", ordered_frnd_list)]:
        print_statement = " {}  >>     Your Preference is: ".format(user_type)
        print_statement += ", ".join(user_list)
        print(print_statement)

except ValueError as ve2:
    print("ValueError: A non number value was detected. Please check all inputted numbers are numbers")
    print("Exception message:", ve2)

finally:
    print(" Completed User preference program. Thanks You for your input")



# big small medium large xlarge
# big small medium large xlarge huge
# big small medium large 
# big small 1 large xlarge
# bi4 small medium large xlarge
# 5 3 1 4 2
# 1 3 5 2 4
# text_ans = [item for item in user_items_list if not item.isdigit()]
# print(text_ans)
 


