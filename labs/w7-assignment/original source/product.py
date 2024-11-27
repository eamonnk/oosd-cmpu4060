'''
Week 5- Classes - 2 of 3 files

--product.py--
-eamonn kelly
'''

class Product:

# Constructor to define product attributes
    def __init__(self, n:str, d:str, s:int):
        self.name=n
        self.description=d
        self.stock=s

# Function to print, print all is default parameter when and
# formatting is handled in the print statements
    def print(self):
        print("Product name is: ", self.name)
        print("Product Description is: ", self.description)
        print("Stock number is: ", self.stock)
        print("----------")


