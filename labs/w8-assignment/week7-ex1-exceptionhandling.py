# Week 2 - Ex 3 - item reordering

REQ_LIST_LEN =3
# Prompt user to input their full name with space between them
user_items_list=input("Please enter a list of {} items to be rated, separated by spaces: ".format(REQ_LIST_LEN)).split()
print(user_items_list)
# text_ans = [item for item in user_items_list if not item.isdigit()]
# print(text_ans)

# for items in user_items_list:
#     if items.isdigit():
#         print("items must be text based items not numbers. PLease enter text bases items to be rated.")
# else:
#     print(list(enumerate(user_items_list, start=1)))

# for index, items in user_items_list:
#     print(index, items)

# convert string to list item
#user_items_list=user_items_str.split()
#itemList = input("Please the list of 5 items to be rated, separated by spaces: ").split()
# print("----------------------------\nItem ids:\n1 {2}\n2 {3}\n3 {4}\n4 {5}\n5 {7}\n----------------------------".format(itemList[0], itemList[1], itemList[2], itemList[3], itemList[4]))

# formatted_string = "Name: {age}, Age: {name}".format(name="Alice", age=30)
# print(formatted_string)


# print(user_items_list)


# for items in user_items_list:
    


# for items in user_items_list:
#     print(sorted(user_items_list))
    
# item_display=("1 "+ user_items_list[0] + "\n" +
#                 "2 " + user_items_list[1] + "\n" +
#                     "3 " + user_items_list[2] + "\n"
#                         +"4 " + user_items_list[3] + "\n"
#                             +"5 " + user_items_list[4] + "\n")
# print(item_display)

# # get user and friend preferences
# user_pref_str=input("User - Please enter the item ids in order of your preference for the items, separated by spaces: ")
# friend_pref_str=input("Friend - Please enter the item ids in order of your preference for the items, separated by spaces: ")

# # convert user preferences from string to list item
# user_pref_list=user_pref_str.split()
# friend_pref_list=friend_pref_str.split()

# # Identify the first to fifth elements or preferences and assign them to variables
# user_first_pref_str=user_pref_list[0]
# user_second_pref_str=user_pref_list[1]
# user_third_pref_str=user_pref_list[2]
# user_fourth_pref_str=user_pref_list[3]
# user_fifth_pref_str=user_pref_list[4]

# # convert preference values string item values to Integer variables
# user_first_pref_int=int(user_first_pref_str)
# user_second_pref_int=int(user_second_pref_str)
# user_third_pref_int=int(user_third_pref_str)
# user_fourth_pref_int=int(user_fourth_pref_str)
# user_fifth_pref_int=int(user_fifth_pref_str)

# # Display output to user of their preferences
# print("\n" + "User - The items ordered by your preference were: " + "\n"
#         + "1st" + " " + user_items_list[(user_first_pref_int)-1] + "\n"
#             +  "2nd" + " " + user_items_list[(user_second_pref_int)-1] + "\n"
#                 + "3rd" + " " + user_items_list[(user_third_pref_int)-1] + "\n"
#                     +  "4th" + " " + user_items_list[(user_fourth_pref_int)-1] + "\n"
#                         + "5th" + " " + user_items_list[(user_fifth_pref_int)-1] + "\n")


# # Identify the first to fifth elements of friend preferences and assign them to variables
# friend_first_pref_str=friend_pref_list[0]
# friend_second_pref_str=friend_pref_list[1]
# friend_third_pref_str=friend_pref_list[2]
# friend_fourth_pref_str=friend_pref_list[3]
# friend_fifth_pref_str=friend_pref_list[4]

# # convert preference values string item values to Integer variables
# friend_first_pref_int=int(friend_first_pref_str)
# friend_second_pref_int=int(friend_second_pref_str)
# friend_third_pref_int=int(friend_third_pref_str)
# friend_fourth_pref_int=int(friend_fourth_pref_str)
# friend_fifth_pref_int=int(friend_fifth_pref_str)

# # Display output to user of their preferences
# print("\n" + "Friend  - The items ordered by your preference were: " + "\n"
#         + "1st" + " " + user_items_list[(friend_first_pref_int)-1] + "\n"
#             +  "2nd" + " " + user_items_list[(friend_second_pref_int)-1] + "\n"
#                 + "3rd" + " " + user_items_list[(friend_third_pref_int)-1] + "\n"
#                     +  "4th" + " " + user_items_list[(friend_fourth_pref_int)-1] + "\n"
#                         + "5th" + " " + user_items_list[(friend_fifth_pref_int)-1] + "\n")