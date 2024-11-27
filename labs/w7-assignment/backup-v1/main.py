'''
Week 7- Exception handling - Ex 2 - 1 of 3 files

--main.py--
-eamonn kelly
'''

# import classes from product and shop
from product import Product
from shop import Shop

DATA = [
    ["milk", "Fresh from the farm", 1],
    ["bread", "Fresh from the baker", 3],
    ["tea", "Box of 100 teabags", 5],
    ["eggs", "A dozen per box", 7],
    ["ice cream", "1l box, vanilla", 9]
]

##--- To test each area you can un-comment and re-comment the lines in each section as needed,
##--- and progress down through each section---###

# -- 1 --
# --Initial Test product functionality - enter a valid product and print out product details---
print(" -- 1 --")
p1=Product("rice", "tasty in 100g", 0,)
p1.print()

#-- 2--
#----product name passed into the Product constructor is an empty string----
# Lines in this section need to be un-Commented to run and other sections commented. Must be re-commented after running.
# Apologies this is not runnable - have to Un-Comment lines in this section to run it. It was justtakign me a long time to write ti runnable and had to modify exception handlgin in produict def and was taking a liogn tim and had to cut my loses.

# exception codeis in product.py in productvclass definition. If empty string valeu is entered an exception is raised and get the msg
# "Product name is empty. Product name cannot be empty.Please Enter a valid product name")

print(" -- 2 -- ")
num_tries_1a=0
while num_tries_1a <= 1:
    if num_tries_1a < 1:
        p2=Product("", "tasty in 100g", 3,)
        num_tries_1a += 1
        continue
    else:
        p3=Product("pizza", "tasty in 500g slices", 3,)
        p3.print()
        break

#-- 3 --
#----stock value passed into the Product constructor is 'not' a non-negative integer----
# seems an odd one but hopefully am reading spec right that stock gives error if number is "not" a non-negative integer 
# i.e. stock value has to be a negative integer
print(" -- 3 -- ")
num_tries_2a=0
while num_tries_2a <= 1:
    if num_tries_2a < 1:
        p4=Product("coconut", "fresh daily from tropical island", -3,)
        num_tries_2a += 1
        continue
    else:
        p5=Product("coconutier", "fresh daily from tropical island", 3,)
        p5.print()
        break
# # #-- 4 --
print(" -- 4 --")
p6=Shop(DATA)
p6.print_product_list()

print("-----")
num_tries_3a=0
while num_tries_3a <= 1:
    if num_tries_3a < 1:
        p6.remove_product('breadcrumbs')
        num_tries_3a += 1
        continue
    else:
        p6.remove_product('bread')
        p6.print_product_list()
        break




#