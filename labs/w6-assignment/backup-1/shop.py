# '''
# Week 6 - Assignment -
# Class Inheritance - 3 of 3 files

# --shop.py--
# -eamonn kelly
# '''
from product import Product, FoodProduct
from datetime import datetime
from datetime import timedelta

#define variables
prods_div_line="----------------------------------------"
prods__div_line_header="---------------Products-----------------"
prods_low_stock_div_line="--------------Low Stock-----------------"
foodprods_div_line="-------------------------------------------------------------------"
foodprods_div_line_header="--------------------------Food Products----------------------------"
foodprods_low_stock_div_line="----------------------------Low Stock------------------------------"
foodprods_out_of_date_div_line="---------------------------Out of Date-----------------------------"
header_welcome_txt="Welcome to "
stock_column_headers = ['Name', 'Low Stock Mark', 'Stock', 'Expiry Date']
out_of_stock="Out of Stock"
no_prods_text="-- There are no products in listed in your shop: --"
print_option_error_msg="Only print options available are \n \" \"  (blank) - to print all products,\n \"od\" - to print out of date products \n \"ls\"- to print low stock products"


class Shop:

# created empty list to store products and used lambda function to map data lists items to the shop products list.
# Product objects are defined by number of elements in their data, 
# with Products containing 3 elements and Food Products containing 4 values.
# we use len to determine that number
    def __init__(self, n:str, sp):
        self.__name=n
        self.__stockedProducts=sp
        
        self.__stockedProducts=[]
        self.__stockedProducts = list(map(lambda prod: Product(prod[0], prod[1], prod[2]) \
            if len(prod) < 4 else FoodProduct(prod[0], prod[1], prod[2], prod[3], prod[4], prod[5]), sp))
        print("You have successfully added data to shop constructor: ")


# used isinstance to check for items which are Product and Food Product Objects in the shop prod list. 
# Tried to use len but len is not a defined method in the classes, so chose this as adding it was not in spec.
# Do additional logic checks to differentiate between the two classes Products and Food Products, 
    def print_product_list(self, filter=""):

# Print "" - default print option
# print Store Site Header using name variable enteres by user at runtime  i.e. self.name
        if filter == "":        
            print('{:<40}'.format(prods_div_line) + '\n'
                + '{:^40}'.format(header_welcome_txt)  + '\n'
                    + '{:^40}'.format(self.__name)  + '\n'
                        + '{:<40}'.format(prods_div_line) + '\n')

# print out msg if no products in the store
            if not self.__stockedProducts:
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
# Have to use the format _Product__name as the values for name, lowstockmark, stock are private 
# need a second condition for Foodproduct as FoodProducts are Products also and will display otherwise
            for items in self.__stockedProducts:
                if isinstance (items, Product) and not isinstance(items, FoodProduct):
                    print('{:<15}'.format(items._Product__name),
                            '{:<20}'.format(items._Product__lowstockmark),
                                '{:<20}'.format(items._Product__stock))

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
# this uses strftime from datetime to change date format
            for items in self.__stockedProducts:
                if isinstance (items, FoodProduct): 
                    exp_date_modified=str(items._FoodProduct__useByDate.strftime("%d-%m-%Y"))
                    print("{:<15}".format(items._Product__name),
                            '{:<20}'.format(items._Product__lowstockmark),
                                '{:<10}'.format(items._Product__stock),
                                    '{:<20}'.format(exp_date_modified))

# --Print when 'od' filter is used--
# only filtering Food Products as only they have expiry date attribute
        elif filter == "od": 
            #Print Shope Header
            print('{:<40}'.format(prods_div_line) + '\n'
                + '{:^40}'.format(header_welcome_txt)  + '\n'
                    + '{:^40}'.format(self.__name)  + '\n'
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
            for items in self.__stockedProducts:
                if isinstance (items, FoodProduct) and items.is_out_of_date(): 
                    exp_date_modified=str(items._FoodProduct__useByDate.strftime("%d-%m-%Y"))
                    print("{:<15}".format(items._Product__name),
                            '{:<20}'.format(items._Product__lowstockmark),
                                '{:<10}'.format(items._Product__stock),
                                    '{:<20}'.format(exp_date_modified))

# --Print when 'ls' filter is used--
        elif filter == "ls":        
            print('{:<40}'.format(prods_div_line) + '\n'
                + '{:^40}'.format(header_welcome_txt)  + '\n'
                    + '{:^40}'.format(self.__name)  + '\n'
                        + '{:<40}'.format(prods_div_line) + '\n')

# print out msg if no products in the store
            if not self.__stockedProducts:
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

# print Product objects for low stock
# used isinstance to just grab the Product object type
            for items in self.__stockedProducts:
                if isinstance (items, Product)and not isinstance(items, FoodProduct) and items.stock_is_low():
                    print("{:<15}".format(items._Product__name),
                            '{:<20}'.format(items._Product__lowstockmark),
                                '{:<20}'.format(items._Product__stock))

# Print FoodProducts objects for low stock
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

# print out the FoodProduct objects for low stock
# Used isinstance to filter the object type and modified useByDate to be more user readable
            for items in self.__stockedProducts:
                if isinstance (items, FoodProduct) and items.stock_is_low(): 
                    exp_date_modified=str(items._FoodProduct__useByDate.strftime("%d-%m-%Y"))
                    print("{:<15}".format(items._Product__name),
                            '{:<20}'.format(items._Product__lowstockmark),
                                '{:<10}'.format(items._Product__stock),
                                    '{:<20}'.format(exp_date_modified))
            
            
        elif filter != "" or "od" or "ls":
            print(print_option_error_msg)

    def generate_messages(self):
        print('{:<40}'.format(prods_div_line) + '\n'
                + '{:^40}'.format(header_welcome_txt)  + '\n'
                    + '{:^40}'.format(self.__name)  + '\n'
                        + '{:<40}'.format(prods_div_line) + '\n')
        # for items in product list, Product Objects and stock_is_low() method is True print the msg
        # This will display both Products and FoodProduct objects
        for items in self.__stockedProducts:
            if isinstance (items, Product) and items.stock_is_low():
                print("{} is low on stock. It has {} stock units. \n".format((items._Product__name).upper(), items._Product__stock))

        # for Food Product objects that meet the condition is out of date is 'True' print the message
        # use date time to calculate difference between todays date and exp date and display in message
        for items in self.__stockedProducts:
            if isinstance (items, FoodProduct) and items.is_out_of_date():
                exp_days=(datetime.today()-items._FoodProduct__useByDate).days
                print("{} has passed its expiry date. It is {} day/s passed it's expiry date. \n".format((items._Product__name).upper(), exp_days))

# using * in argument to allow variable length arguments be input in data and avoid errors
# iterating through item or list of items and checking if it is in valid form for Product or Food Product objects
#  if it is in valid form it appends to existing shop list of products   
    def add_product(self, *ap ):
        self.addprod=ap
        print(ap)

# If item being added is already an Product or FoodProduct object append it to existing list
# tried to do this way first but modified to lambda expression and left this option in for error handling
# else create a list of objects to be added and classify them as Product or Food Product based on len of items present 
# Product has 3 and Food Product has 6 
        for item in ap:
            if isinstance(item, (Product, FoodProduct)): 
                print("isisisisi")
                self.__stockedProducts.append(item)
            else:
                # empty list which will contain product to append to existing product list
                self.addprod=[]
                self.addprod=ap
                self.addprod = list(map(lambda prod: Product(prod[0], prod[1], prod[2]) \
                    if len(prod) < 4 else FoodProduct(prod[0], prod[1], prod[2], prod[3], prod[4], prod[5]), ap))
# for loop to iterate through 
                for item in self.addprod:
                    self.__stockedProducts.append(item)
                print("22222")

    # def add_product(self, name, description, stock):
    #     added_prod= Product(name, description, stock)
    #     self.shopProducts.append(added_prod)
    #     print(f"You have successfully added the product {name} to the shop.")


# Used for loop to iterate through the shop product list, converted all names to lower case to remove case issues
# removed product using remove method and printed statement saying product was removed. The exited function using break so as not 
# to run the following if statement
# used removed item flag so could call a print statement outside of the loop and notify user product name ahs nto been found
    def remove_product(self, n=str):
        self.name=n
       
       #rem_prod_name=input("Please enter the name of the product you wish to remove? ")
       #rem_prod_name.lower()
        removed_item_flag = False
        for item in self.__stockedProducts:
                if self.name.lower() == item._Product__name.lower():
                    self.__stockedProducts.remove(item)
                    print("Product {} has been deleted ".format(self.name))
                    removed_item_flag = True
                    break
 
        if removed_item_flag  == False:
            print("Product {} does not exist. Please try again: ".format(self.name))


# restock method, arguments name and a stock value int are expected in input
# use a for loop to check name exists, if it does we set restocked flag to True, otherwise it is defautl and remains False
# if product name does nto exist we get msg saying it does nto exist
    def restock(self, n:str, s:int):
        self.name=n
        self.stock=s
        
        restock_prod=[]
        restocked_prod_flag = False

        for item in self.__stockedProducts:
                if self.name.lower() == item._Product__name.lower():
                    item._Product__stock += self.stock
                    print("Product {} has been updated by {} units: ".format(self.name.upper(), self.stock))
                    restocked_prod_flag = True
                    break
 
        if restocked_prod_flag  == False:
            print("Product {} does not exist. Please try again to update a product stock: ".format(self.name))
 
    def sell(self, n:str, s:int):
        self.name=n
        self.sell_num=s    
        
        sell_prod=[]
        sell_prod_flag = False

        for item in self.__stockedProducts:
                if self.name.lower() == item._Product__name.lower():
                    if self.sell_num <= item._Product__stock:
                        item._Product__stock -= self.sell_num
                        print('\n')
                        print(" {} Units of Product {} have been sold. There are now {} units remaining in stock ".format(self.sell_num, self.name, item._Product__stock))
                        print('\n')
                        sell_prod_flag = True
                        break
                    else:
                        print("There are not enough Units for the required sale. Please choose a sell quantity less than or equal to the product stock. \n There are {} units of {} remaining in stock ".format(item._Product__stock, item._Product__name))
                    
 
        if sell_prod_flag  == False:
            print("Product {} does not exist. Please try again to update product for units sold. ".format(self.name))