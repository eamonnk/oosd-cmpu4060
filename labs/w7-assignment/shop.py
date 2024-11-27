'''
Week 7- Exception handling - Ex 2 - 3 of 3 files

--shop.py--
-eamonn kelly
'''

#import product class as is required for functionality
from product import Product

class ProductNotInList(Exception):
    pass

class Shop:

# define shop products (sp) as empty list in constructor as the object we will load data into
# then used mapping to populate the product list
# finallyu a print statement to provide user with info so they know it is done.
    def __init__(self, sp):
        self.shopProducts=[]
        self.shopProducts=list(map(lambda prod: Product(prod[0], prod[1], prod[2]), sp ))
        print("You have successfully added data to shop constructor: ")

# added the parameters as outlined in the assignment
# then used append method to add to the product data
    def add_product(self, name, description, stock):
        added_prod= Product(name, description, stock)
        self.shopProducts.append(added_prod)
        print(f"You have successfully added the product {name} to the shop.")

## added the parameter as outlined in the assignment
# used lambda function to
    def remove_product(self, name):
        
        # num_tries_3 = 0
        
        # while num_tries_3 < 2:
        
        prod_in_list_flag=False
        
        try:
            for items in self.shopProducts:
                if items.name.lower() == name.lower():
                    print("You have entered a valid product name. It will now be removed from the product list.")
                    prod_in_list_flag = True
                    break
            if not prod_in_list_flag:
                raise ProductNotInList("Product name is not on the product list. Please enter a valid product name.")
        except ProductNotInList as pe1:
                print(" -->> Product not in list exception catch - product name does not match list of available products")
                
        try:
            if prod_in_list_flag:
                index=list(map(lambda sp: sp.name, self.shopProducts)).index(name)
                self.shopProducts.pop(index)
                print(f"You have successfully removed {name} from the shop.")
        except ProductNotInList as pe2:
            print(" -->> Product not in list exception catch ")
            

# default to print all, enumerate list to get it
# did not add index value as wasn't asked for in spec
# used the print f functionality as seems to be a bit cleaner
    def print_product_list(self):
        if not self.shopProducts:
            print("There are no products in listed in your stock: ")
        else:
            for product in self.shopProducts:
                print(f"Name: {product.name}")
                print(f"Description: {product.description}")
                print(f"Stock: {product.stock}")
                print("---------")

    def print_low_on_stock(self):
        prod_min_num=3
        low_stock_list=[]
        low_stock_list=list(filter(lambda product: product.stock < prod_min_num, self.shopProducts))
        print("------------------------------------------------------------------")
        print("the following products are low on stock, i.e. less than 3 in stock")
        print("------------------------------------------------------------------")
        if low_stock_list:
            # print("the following products are low on stock")
            for product in low_stock_list:
                print(f"Name =  {product.name}," + "\n"
                    + f"Description =  {product.description}," "\n"
                        + f"Stock = {product.stock}")
                print("---------")
        elif low_stock_list !=True:
            print("There are no products low on stock i.e. less than 3: ")
