# '''
# Week 6 - Assignment -
# Class Inheritance - 3 of 3 files

# --shop.py--
# -eamonn kelly
# '''
from product import Product, FoodProduct

#define variables
prods_div_line="----------------------------------------"
prods__div_line_header="---------------Products-----------------"
prods_low_stock_div_line="--------------Low Stock----------------"
foodprods_div_line="-------------------------------------------------------------------"
foodprods_div_line_header="--------------------------Food Products----------------------------"
foodprods_low_stock_div_line="----------------------------Low Stock------------------------------"
foodprods_out_of_date_div_line="---------------------------Out of Date-----------------------------"
website_header="Products to Buy - Get Your Products!"
stock_column_headers = ['Name', 'Low Stock Mark', 'Stock', 'Expiry Date']
out_of_stock="Out of Stock"
no_prods_text="-- There are no products in listed in your shop: --"


class Shop:

# created empty list to store products and used lambda function to map data lists items to the shop products list.
# Product objects are defined by number of elements in their data, 
# with Products containing 3 elements and Food Products containing 4 values.
# we use len to determine that number
    def __init__(self, sp):
        self.shopprods=[]
        self.shopprods = list(map(lambda prod: Product(prod[0], prod[1], prod[2]) \
            if len(prod) < 4 else FoodProduct(prod[0], prod[1], prod[2], prod[3], prod[4], prod[5]), sp))
        print("You have successfully added data to shop constructor: ")


# used isinstance to check for items which are Product and Food Product Objects in the shop prod list. 
# Tried to use len but len is not a defined method in the classes, so chose this as adding it was not in spec.
# Do additional logic checks to differentiate between the two classes Products and Food Products, 
    def print_product_list(self, filter=""):

# print Store Site Header when default print filter option is chosen i.e. ""
        if filter == "":        
            print('{:<40}'.format(prods_div_line) + '\n'
                + '{:^40}'.format(website_header)  + '\n'
                    + '{:<40}'.format(prods_div_line) + '\n')

# print out msg if no products in the store
            if not self.shopprods:
                print()
                print(no_prods_text)
                print()
                return

# Print out store UI 
# variables used are defined above to separate out from the code
            print(prods_div_line)
            print(prods__div_line_header)
            print(prods_div_line)
            print('{:<15}'.format(stock_column_headers[0])
                    + '{:<20}'.format(stock_column_headers[1])
                        + '{:<20}'.format(stock_column_headers[2]))

# print Product objects
# used isinstance to just grab the Product object type
            for items in self.shopprods:
                if isinstance (items, Product)and not isinstance(items, FoodProduct):
                    print("{:<15}".format(items.name),
                            '{:<20}'.format(items.lowstockmark),
                                '{:<20}'.format(items._stock))

# Print FoodProducts objects
# print a blank line anf then the title and headers for FooProducts
# Again used isinstance to filter the FoodProduct Object types
# There is an additional item int he list of item attributes , namely expiry date
            print()
            print(foodprods_div_line)
            print(foodprods_div_line_header)
            print(foodprods_div_line)
            print('{:<15}'.format(stock_column_headers[0])
                    + '{:<20}'.format(stock_column_headers[1])
                        + '{:13}'.format(stock_column_headers[2])
                            + '{:<20}'.format(stock_column_headers[3]))

# print out the FoodProduct objects using default print option ""
# Used isinstance to filter the object type and modified useByDate to be more user readable
# this uses strftime from datetime 
            for items in self.shopprods:
                if isinstance (items, FoodProduct): 
                    exp_date_modified=str(items.useByDate.strftime("%d-%m-%Y"))
                    print("{:<15}".format(items.name),
                            '{:<20}'.format(items.lowstockmark),
                                '{:<10}'.format(items._stock),
                                    '{:<20}'.format(exp_date_modified))

# --Print when 'od' filter is used--
# only filtering Food Products as only they have expiry date attribute
        elif filter == "od": 
            #Print Shope Header
            print('{:<40}'.format(prods_div_line) + '\n'
                + '{:^40}'.format(website_header)  + '\n'
                    + '{:<40}'.format(prods_div_line) + '\n')
            
            #Print FoodProduct objects
            print()
            print(foodprods_div_line)
            print(foodprods_div_line_header)
            print(foodprods_out_of_date_div_line)
            print(foodprods_div_line)
            print('{:<15}'.format(stock_column_headers[0])
                    + '{:<20}'.format(stock_column_headers[1])
                        + '{:<13}'.format(stock_column_headers[2])
                            + '{:<20}'.format(stock_column_headers[3]))
            for items in self.shopprods:
                if isinstance (items, FoodProduct) and items.is_out_of_date(): 
                    exp_date_modified=str(items.useByDate.strftime("%d-%m-%Y"))
                    print("{:<15}".format(items.name),
                            '{:<20}'.format(items.lowstockmark),
                                '{:<10}'.format(items._stock),
                                    '{:<20}'.format(exp_date_modified))

# --Print when 'ls' filter is used--
        if filter == "ls":        
            print('{:<40}'.format(prods_div_line) + '\n'
                + '{:^40}'.format(website_header)  + '\n'
                    + '{:<40}'.format(prods_div_line) + '\n')

# print out msg if no products in the store
            if not self.shopprods:
                print()
                print(no_prods_text)
                print()
                return

# Print out store UI 
# variables used are defined above to separate out from the code
            print(prods_div_line)
            print(prods__div_line_header)
            print(prods_low_stock_div_line)
            print(prods_div_line)
            print('{:<15}'.format(stock_column_headers[0])
                    + '{:<20}'.format(stock_column_headers[1])
                        + '{:<20}'.format(stock_column_headers[2]))

# print Product objects
# used isinstance to just grab the Product object type
            for items in self.shopprods:
                if isinstance (items, Product)and not isinstance(items, FoodProduct) and items.stock_is_low():
                    print("{:<15}".format(items.name),
                            '{:<20}'.format(items.lowstockmark),
                                '{:<20}'.format(items._stock))

# Print FoodProducts objects
# print a blank line anf then the title and headers for FooProducts
# Again used isinstance to filter the FoodProduct Object types
# There is an additional item int he list of item attributes , namely expiry date
            print()
            print(foodprods_div_line)
            print(foodprods_div_line_header)
            print(foodprods_low_stock_div_line)
            print(foodprods_div_line)
            print('{:<15}'.format(stock_column_headers[0])
                    + '{:<20}'.format(stock_column_headers[1])
                        + '{:13}'.format(stock_column_headers[2])
                            + '{:<20}'.format(stock_column_headers[3]))

# print out the FoodProduct objects using default print option ""
# Used isinstance to filter the object type and modified useByDate to be more user readable
            for items in self.shopprods:
                if isinstance (items, FoodProduct) and items.stock_is_low(): 
                    exp_date_modified=str(items.useByDate.strftime("%d-%m-%Y"))
                    print("{:<15}".format(items.name),
                            '{:<20}'.format(items.lowstockmark),
                                '{:<10}'.format(items._stock),
                                    '{:<20}'.format(exp_date_modified))
            
            

       
