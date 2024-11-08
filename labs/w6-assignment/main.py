from product import Product, FoodProduct
from shop import Shop


# # ---- Scenario 1 - Product and FoodProduct CLass Testing----------
# -- 1 ---- Add product to Product and Food Product objects and test print and class methods for those classes---
# create an instance of Product class p1, and call the print method within the product class
# The output is the product attributes
print("----------------------Scenario 1----Product and FoodProduct CLass Testing----------------------")
print("--1--")
p1=Product("teapot", 5, 4)
p1.print()
# -- 2.2 --- Call the product class get_name() method
# output will display the name of the product in a print statement containing the get_name method call
# we have defined a print statement in the method that is called aswell as a print statement here that includes the get_name() method. 
# Hence it will appear four times, this is just to demonstrate # the various ways it can be called and displayed.
print("--2--")
p1.get_name()
print("The product name is {}".format(p1.get_name()))
# -- 3 ---Call the product class get_stock()) method
# method contains a print statement within it, and we also include the method call in a print statement here, 
# hence we get multiple print outs for the data value in the different print statements
print("--3--")
print("The stock amount for {} is - {}".format(p1.get_name(), p1.get_stock()))
p1.get_stock()
# -- 4 ---Call the product class get_stock() method
# we look at the stock value for an item before and after, specificying the value in between the print outs
# scroll back up to see the output and notice the stock number value is now te value you entered
# there is also additional print statements called from within th e method to provide more data and context 
print("--4--")
p1.print()
p1.set_stock()
p1.print()
# -- 5 --- Call the product class is_perishable() method
# the sample product here is a product class object, as such it is not perishable and will return False
# we only use the method here as part of the print statement
print("--5--")
print("{} is perishable:  - {}".format(p1.get_name().upper(), p1.is_perishable()))
# -- 6 -- Call the product class stock_is_low method 
# we check the stock value against the low stock mark and if it is less than or equal to it it will be True for stock is low
# this statement will print True for stock is low
print("--6--")
p1.stock_is_low()
print("Stock is low for Product {}: - {}. ".format(p1.get_name(), p1.stock_is_low(), p1.get_stock()))
# --------Food Product ------
# -- 7 -- create an instance of FoodProduct with the below input
# we do not print out the product list as we did not create a print method for food product as per the spec.
# we will print out the full product list later int he sho class
# we will receive a print statement just saying we have successfully added a food product object and list the expiry date to prove it.
print("--7--")
p2=FoodProduct("milk", 5, 4, 2024, 11, 10)
print("No error was generated and as such You have successfully added a Food Product object")
#------
#-- 8 --Call the Food Product class is_perishable method 
# we added a milk product  earlier and that contained a useByDate, which means it is perishable
# As such we will be returned True value here.
print("--8--")
p2.is_perishable()
print("Product is Perishable : - {}  ".format(p2.is_perishable()))
#-- 9 --Call the Food Product class is_out_of_date() method 
# we use self.__useByDate < datetime.today() in the method, our date is beyons todays date and as such
# we will be returned ais out of dat value of False
print("--9--")
p2.is_out_of_date()
print("The use By Date has passed : T/F : - {} ".format(p2.is_out_of_date()))

#------------------end of Product and Food Product method and functionality testing------------------
# if you wish you cna block comment all lines above this section if you need to run the main file several times 
#---------------------------------------------------------------------------------------------
#---Scenario 2----Shop Class Testing ---------------------------------------------------------------------
print("------------------------------------------------------------------------------")
print("----------------------Scenario 2----Shop Class Testing------------------------")
print("------------------------------------------------------------------------------")
# a set of products in nested list. some lists have 3 values and some have 6 values
DATA_1=[]
DATA = [
    ["teapot", 4, 2],
    ["table", 5, 2],
    ["bed", 3, 5],
    ["milk", 3, 10, 2024, 11,21],
    ["bread", 3, 2, 2024, 10,4],
    ["tea", 3, 1, 2024, 11,9],
    ["cake", 3, 12, 2024, 11, 6],
]

# Import data set, create relevant product objects and print them out
# --2.1--import empty list and try print product list
# First with an empty products list i.e. DATA_1 is a list containing no values
# we get the shop UI displaying and a msg saying no products in the shop
# we use the name My Shop for thew shop name
print("--2.1--")
myshop=Shop('My Shop', DATA_1)
myshop.print_product_list("")
#---
#-- 2.2- print_product_list ''
# default is to print all i.e. "" in the print_product_list() method
# we get all Products and FoodProducts printed out. They are split into a section for each
print("--2.2--")
myshop=Shop('My Shop', DATA)
myshop.print_product_list("")
# #---
#-- 2.3 -  print_product_list 'od'
# now print products that are out of date using 'od' value
# This will print out objects which are out of date only
# ONly FoodProduct objects have useByDate attributes, as such only Food Product Items which are expired will be printed out
print("--2.3--")
myshop.print_product_list("od")
#---
#-- 2.4-  print_product_list 'ls'
# now print products products for which the stock is low using 'ls' value
# there will be a section for Products and a section for FoodProducts 
# and only items who's stock value is less than low stock mark will be printed
# these values can be modified in DATA nested list set above if needed
print("--2.4--")
myshop.print_product_list("ls")
#---
#--  2.5 --generate message
# using generate_message() method print a message for each low stock and out of date products and Food Product objects
# returns messages stating the items affected and some details.
# we converted names to upper to make it easier to read name, as well as the number of days passed its expiry date
# this was done using datetime
print("--2.5--")
myshop.generate_messages()
#---
#-- 2.6 -- add product
# add a list object with 3 arguments for name, lowstock mark and stock number using the add_product() method
# we see the product added to Product list, like wise we add an item with an expiry date and we see that 
# added to the Food Products list also. we called print once after each addition. As such yo may need to scroll to see added product
print("--2.6--")
myshop.add_product(['football', 10, 12])
myshop.print_product_list("")
myshop.add_product(['cheese', 10, 12, 2025, 5, 14])
myshop.print_product_list("")
#---
#-- 2.7 -- remove product
# view all products before hand, then remove bread and print all products after.
# bread item is no longer present. It has been removed and we receive a msg confirming that also.
# try to remove a product that does not exist. You get an error message saying product x does nto exist
print("--2.7--")
myshop.print_product_list("")
myshop.remove_product("bread")
myshop.print_product_list("")
myshop.remove_product("breadier")

# -- 2.8 restock
# print and view product list first, then run restock method specifying expected arguments str and int
# view product list again cake units have increased by specified amount.a msg stating this is also received.
# Also, try remove product that does tno exist and get an error message saying product does not exist, in last line
print("--2.8--")
myshop.print_product_list("")
myshop.restock('cake', 5)
myshop.print_product_list("")
myshop.restock('breadier', 4)

# -- 2.9 --sell
# print and view product list, run sell method specifying expected arguments str and int
# view product list again cake message stating how many were sold and what stock units are left
# try to sell more units than exist in stock > you get a message stating you cannot sell them as there are not enough
# Try to sell product that does not exist > get error message  as try to restock product that does nto exist as in last line
print("--2.9--")
myshop.print_product_list("")
myshop.sell('cake', 3)
myshop.print_product_list("")
myshop.sell('cake', 50)
myshop.sell('cakeier', 50)



