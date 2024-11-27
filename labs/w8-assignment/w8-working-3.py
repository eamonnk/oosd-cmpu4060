# ' '.join(["a", "b", "c"])
# ''.join(["A", "n", "n"])
# separator = ", "
# list = ["python", "javascript", "java"]
# print(separator.join(list))

REQ_LIST_LEN = 5

num_tries_2 = 0

valid_list_range=list((range(1, REQ_LIST_LEN+1, 1)))
print(valid_list_range)
print(type(valid_list_range))
print("aaaaaaaa")
valid_list_range_str = [str(item) for item in valid_list_range]
print(valid_list_range_str)
print(type(valid_list_range_str))
print("bbbbnnnnn")

# use sorted as it doesn't modify the list, we need it as is.
#while num_tries_2 < 2:
user_pref=input("User > Please enter the item ids in order of your preference for the items, separated by spaces: ").split()
print(user_pref)
print("zzzzz")#
print(valid_list_range_str)
if sorted(user_pref) == sorted(valid_list_range_str):
    print(" they are equal")
else:
    print("theyare not")

# print(user_pref)
#     print(valid_list_range_str)
#     print("111111")
# # for u_items in user_pref:
#     if valid_list_range_str != user_pref:
#         print("User - You have entered values not in range. You must enter values between 1 and {} ".format(REQ_LIST_LEN))
#         num_tries_2 += 1
#         continue
#     else:
#         print("You have entered valid preference")
#         break
    
    
    
# big small medium large xlarge
# big small medium large xlarge huge
# big small medium large 
# big small 1 large xlarge
# bi4 small medium large xlarge
# 5 3 1 4 2
# 1 3 5 2 4
# 1 2 3 4 5