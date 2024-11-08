from product import Product, FoodProduct
from shop import Shop


# # ---- Scenario 1 - Product and FoodProduct CLass Testing----------
# # ---- Add product to Product and Food Product objects and test print and class methods for those classes---
# p1=Product("teapot", 5, 4)
# p1.print()
# # #---
# p1.get_name()
# print("The product name is {}".format(p1.get_name()))
# # #---
# print("The stock amount for {} is - {}".format(p1.get_name(), p1.get_stock()))
# p1.get_stock()
# # -----
# # p1.set_stock()
# # p1.print()
# # -----
# p1.is_perishable()
# print("{} is perishable:  - {}".format(p1.get_name(), p1.is_perishable()))
# # ---
# p1.stock_is_low()
# print("Stock is low for Product {}: - {}. ".format(p1.get_name(), p1.stock_is_low(), p1.get_stock()))
# # --------Food Product ------
# # comment the above and un-comment the below ans step through then
# p2=FoodProduct("milk", 5, 4, 2024, 11, 10)
# #------
# ##don't have and print, get_name methods etc defined specifically for Food Product objects as per the spec
# # so just showing methods in the spec here

# p2.is_perishable()
# print("Product is Perishable : - {}  ".format(p2.is_perishable()))

# p2.is_out_of_date()
# print("The use Bty Date has passed : T/F : - {} ".format(p2.is_out_of_date()))

#------------------end of Product and Food Product method and functionality testing------------------
#---------------------------------------------------------------------------------------------
#---Scenario 2----Shop Class Testing ---------------------------------------------------------------------

# # a set of products in nested list. some lists have 3 values and some have 6 values
# DATA_1=[]
DATA = [
    ["teapot", 4, 2],
    ["table", 5, 2],
    ["bed", 3, 5],
    ["milk", 3, 10, 2024, 11,21],
    ["bread", 3, 2, 2024, 10,4],
    ["tea", 3, 1, 2024, 11,9],
    ["cake", 3, 12, 2024, 11, 6],
]

# # Import dat set, create relevant product objects and print them out
# # --1 --First with an empty products list i.e. DATA_1 is a list containing no values
# # we get a msg saying no products in the shop
# myshop=Shop('my shop', DATA_1)
# myshop.print_product_list("")
# #---
# #-- 2- default is to print all i.e. "" in the print_product_list method
# # we get all Products and FoodProducts printed out
myshop=Shop('my shop', DATA)
myshop.print_product_list("")
# #---
# #-- 3 -  now print products that are out of date using 'od' value
# myshop.print_product_list("od")
# #---
# #-- 4-  now print products products for which the stock is low using 'ls' value
# # there will be a section for Products and a section for FoodProducts 
# # and only items who's stock value is less than low stock mark will be printed
# # these values can be modified in DATA nested list set above if needed
# myshop.print_product_list("ls")
# #---

# #--  5 - print a message for low stock and out of date products and Food Product objects
# # returns messages stating the items affected and some details.
# myshop.generate_messages()

# #-- 6 -- add product
myshop.add_product(['Coffee', 10, 12])

# # -- 7 -- remove product
# # viewe all products before hand, then remove bread and print all products after.
# # bread item is no longer present. It has been removed
# # try to remove a product that does nto exist. You get an error message saying product x does nto exist
# myshop.print_product_list("")
# myshop.remove_product("bread")
# myshop.print_product_list("")
# myshop.remove_product("breadier")

# # -- 8 restock
# # print abd view product list, run restock method specifying expected arguments str and int
# # view produc list again cake units have increased by specified amount
# # get error messaga eis try to restock product that does nto exist as in last line
# myshop.print_product_list("")
# myshop.restock('cake', 5)
# myshop.print_product_list("")
# myshop.restock('breadier', 4)

# # -- 9 --sell
# # print abd view product list, run sell method specifying expected arguments str and int
# # view product list again cake message stating how many were sold and what stock units are left
# # try to sell more units than exist in stock > you get a message stating you cannot sell them as there are not enough
# # Try to sell product that dpes not exist > get error message  as try to restock product that does nto exist as in last line
# myshop.print_product_list("")
# myshop.sell('cake', 3)
# myshop.sell('cake', 50)
# myshop.sell('cakeier', 50)



