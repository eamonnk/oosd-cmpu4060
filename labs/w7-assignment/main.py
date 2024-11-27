'''
Week 7- Exception handling - Ex 2 - 1 of 3 files

--main.py--
-eamonn kelly
'''
from product import Product
from shop import Shop

DATA = [
    ["milk", "Fresh from the farm", 1],
    ["bread", "Fresh from the baker", 3],
    ["tea", "Box of 100 teabags", 5],
    ["eggs", "A dozen per box", 7],
    ["ice cream", "1l box, vanilla", 9]
]

##--- main.py is runnable by just clicking run file---
# sections here are broken down into --1--, --2--, --3--, and --4-- sections below as per spec
# error handling is done in product and shop files
# have while loops here to allow main file be runnable when error occur
# also incorrect data included in input here below in each section also to check error handling
# print out of exception catches are included in output here

# -- 1 --
# --Initial Test product functionality - enter a valid product and print out product details---
# this will add a single product then print out the product details once added.
print(" -- 1 --")
p1=Product("rice", "tasty in 100g", 0,)
p1.print()

#-- 2--
#----product name passed into the Product constructor is an empty string----
# Lines in this section need to be un-Commented to run and other sections commented. Must be re-commented after running.
# Apologies this is not runnable - have to Un-Comment lines in this section to run it. It was just taking me a long time to write ti runnable and had to modify exception handling in product def and was taking a long tim and had to cut my loses.

# exception code is in product.py in product class definition. If empty string value is entered an exception is raised and get the msg
# "Product name is empty. Product name cannot be empty.Please Enter a valid product name")

# The below will return two catch errors for empty product errors, then will successfully add a product 

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
#----stock value passed into the Product constructor is 'not' a non-negative integer ie. is a positive int----
# have -3 and + 3 values to check error handling
# i.e. stock value has to be a negative integer
# The below code will catch two not positive number errors then successfully add a product

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

# the below code will add the above DATA nested list of products using the shop product classes
# then print out the list of available products
# It will try to remove the 'breadcrumbs product which does tno exist and the error will be caught by 
# the error handling code and displayed here.
# a product which does exist will then try to be removed, i.e 'bread' and and messages will verify it is removed
# the list of products will ebprinted again with the productv no longer present 

print(" -- 4 --")
p6=Shop(DATA)
p6.print_product_list()

print("-----")
num_tries_3a=0
while num_tries_3a <= 1:
    if num_tries_3a < 1:
        p6.remove_product('breadcrumbs')
        num_tries_3a += 1
        break
p6.remove_product('bread')
p6.print_product_list()

