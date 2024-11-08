from datetime import datetime

# Constructor to define product attributes
# use underscore to define stock as a private attribute which be modified using a setter method
# getter, setter and deleter must access x with a prepended underscore, which from the outside it is accessed a 
# just with normal name as per class notes

class Product:
    def __init__(self, n:str, l:int, s:int):
        self.name=n
        self.lowstockmark=l
        self._stock=s
    
# Function to print, print all is default parameter when and
# formatting is handled in the print statements
    def print(self):
        print("----------")
        print("Product name is: ", self.name)
        print("Product low stock mark is: ", self.lowstockmark)
        print("Stock number is: ", self._stock)
        print("----------")

# method to get the name of a particular product 
    def get_name(self):
        print 
        print("----------")
        print("Product name is: ", self.name)
        print("----------")
        
# using getter, setter and deleter must access x with a prepended underscore, which from the outside it is accessed a just with normal name
# as per class notes

    def get_stock(self):
        print("----------")
        print("There are {},  {} units in stock".format(self._stock, self.name))
        print("----------")

# method to set a stock value for a particular product
    def set_stock(self):
        print("calling setter method")
        new_stock_num=int(input("Please enter a new stock quantity for {} units: ". format(self.name)))
        print(" read in stock num is {} ".format(new_stock_num))
        
        self._stock = new_stock_num
        print(" new stock value is {}.... : ".format(self._stock))

# set a default value for for is_perishable to False, product class is always False. 
# An if else statement will print out the current status
# also return the value of False as the default for is_perishable method
    def is_perishable(self, isperishable=False):
        print("test1")
        self.is_perishable=isperishable
        #state=self.is_perishable
        #print(" value is {} : ". format(self.is_perishable()))
        if self.is_perishable:
            print("The product is perishable")
            print("test2")
        elif not self.is_perishable:
            print("The product is not perishable")
            print("test3")
        return False
    
            
# If lowstockmark is greater than or equal to current stock value returns a False boolean value
# else return a True boolean value
# the boolean is returned in the method depending on scenario
# Low stock value is defined in product definition during run tine for each product

    def stock_is_low(self):
        return self._stock <= self.lowstockmark
        #self.stock_is_low=lowstock=False
        # print("test1")
        # if  self.lowstockmark >= self._stock:
        #     print("The product {} is low on stock. Its has {} items in stock:  ". format(self.name, self._stock ))
        #     print("test2")
        #     return False
        # else:
        #     print("You are not at the low stock mark. You have {} , {} items in stock".format(self._stock, self.name ))
        #     print("test3")
        #     return True
        
# creating class FoodPoduct which is a sub class of of Product 
# adding attribute for use by date which consist of year, month, date(y,m,d)


class FoodProduct(Product):
    def __init__(self, n, l, s, y, m, d):
        super().__init__(n, l, s)
        self.useByDate = datetime(y, m, d)

  
    #def is_perishable(self):
        
# will return True if the useByDate is less that today function in datetime
    def is_out_of_date(self):
        #print(self.useByDate.strftime(%d/%m/%Y))
        return self.useByDate < datetime.today()
        
        