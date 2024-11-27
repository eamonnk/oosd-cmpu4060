'''
Week 7- Exception handling - Ex 2 - #2 of 3 files

--product.py--
-eamonn kelly
'''
class ProductNameEmptystring(Exception):
    pass

class StockValue_non_neg_int(Exception):
    pass

class Product:

#try-except construct to catch invalid product name inputted

# Constructor to define product attributes
    def __init__(self, n:str, d:str, s):
        self.name=n
        self.description=d
        self.stock=s
        
        
        # -- Product name empty error handling---
        # while loop to give user 2 tries to input correct product name
        # Also try except statement to keep the program running if incorrect data is entered and to catch the error
        num_tries_1 = 0
        
        while num_tries_1 < 2:
            try: 
                # if entered product name not null
                if n != "":
                    #print("You have successfully added a product")
                    break
                # if product name is not not null i.e. is empty/null
                else:
                    raise ProductNameEmptystring("Product name is empty. Product name cannot be empty.Please Enter a valid product name \n")
            except ProductNameEmptystring as ve1:
                print("-->> Product name exception catch - empty product name")
                 
            num_tries_1 += 1

        # ---Stock value is not a non-negative integer error handling i.e. is not positive ----
        # while loop to give user 2 tries to input correct product name
        # Also try except statement to keep the program running if incorrect data is entered and to catch the error
        
        num_tries_2 = 0
        while num_tries_2 < 2:
            try: 
                # if entered stock value
                if s >= 0:
                    #print("You have successfully added a product")
                    break
                # if stock value is not a positive number i.e. is empty/null
                else:
                    raise StockValue_non_neg_int("Stock value is 'not' a non negative integer. Product stock value must be a positive number. Zero is considered neither positive or negative and as such is a valid value. Please enter a positive value for stock value")
            except StockValue_non_neg_int as ve2:
                print("-->> Stock value exception catch - not positive number")
                 
            num_tries_2 += 1
                
        



# Function to print, print all is default parameter when and
# formatting is handled in the print statements
    def print(self):
        print("----------")
        print("Product name is: ", self.name)
        print("Product Description is: ", self.description)
        print("Stock number is: ", self.stock)
        print("----------")


