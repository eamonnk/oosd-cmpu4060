'''
Week 5- Classes - 1 of 3 files

--main.py--
-eamonn kelly
'''

# import classes from product and shop
from product import Product
from shop import Shop

DATA = [
    ["milk", "Fresh from the farm", 10],
    ["bread", "Fresh from the baker", 4],
    ["tea", "Box of 100 teabags", 7],
    ["eggs", "A dozen per box", 3],
    ["ice cream", "1l box, vanilla", 2]
]

##--- To test each area you can un-comment and re-comment the lines in each section as needed,
##--- and progress down through each section---###

#----Test product functionality---
# this will add a single product then print out the product details once added.
p1=Product("Rice", "tasty in 100g", 9,)
# p2=Product("sweets", "very sweet in 50g", 8,)
p1.print()
# p2.print()

#----Test shop functionality----

### load data into shop object and print product list
# shop=Shop(DATA)
# shop.print_product_list()
#---------
### add a product
# shop=Shop(DATA)
# shop.add_product("rice", "tasty", 3)
# shop.add_product("sweets", "150g", 8)
# shop.print_product_list()

#---------
### remove a product
# shop=Shop(DATA)
# shop.remove_product('bread')
# shop.print_product_list()
#-----------
### print the list of products
# shop=Shop(DATA)
# shop.print_product_list()
#----------
### print low stock products , products less than 3
# shop=Shop(DATA)
# shop.print_low_on_stock()



# shop.print_product_list()
# shop.add_product("rice", "tasty", 3)
# shop.add_product("sweets", "150g", 8)
# shop.print_low_on_stock()
# shop.remove_product('bread')
# # shop.print()
# shop.print_product_list()
# print("test4")
# shop_instance=Shop()
# Shop.print()
# print("test5")
# shopProducts.print()
# print("test6")
# shop.print()
# print("test7")
#
# #
# print("test1")
# shop = Shop()
# Shop.add_product(rice)
# # shop.add_product(Product("spuds", "very nice", 2))
# # shop.add_product(Product("bricks", "even nicer", 6))
# # print("---------------------------")
# # print("all products")
# # shop.print()
#
# print("test2")
# shop.print()
# print("test3")
# shop.remove_product("Rice")
# print("test4")
# print(" ---Product ---Rice has been removed----")
# shop.print()
# print("test5")
