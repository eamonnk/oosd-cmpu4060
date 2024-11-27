REQ_LIST_LEN = 5
input_1_flag = 0  # Flag to track the number of attempts

while input_1_flag < 2:  # Allow the user to try up to 2 times
    # Prompt user to input their items
    user_items_list = input("Please enter a list of {} items to be rated, separated by spaces: ".format(REQ_LIST_LEN)).split()

    # Check if the number of items entered is correct
    if len(user_items_list) != REQ_LIST_LEN:
        print(f"\nYou have not entered the correct number of items. You should enter exactly {REQ_LIST_LEN} items and all items should be text based.")
        input_1_flag += 1
        continue

    # Check if all items are text (non-numeric)
    if any(item.isdigit() for item in user_items_list):
        print("\nYou have entered numeric items. You need to enter text-based items only.")
        input_1_flag += 1
        continue

    # If input is valid
    print(f"\nYou entered a valid list of items: {user_items_list}")
    break  # Exit the loop after successful input

# If the user failed both attempts
if input_1_flag == 2:
    print("You have entered invalid data twice. Exiting the program.")
    exit()  # Exit the program after two failed attempts
