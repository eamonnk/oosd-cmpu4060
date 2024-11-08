from datetime import datetime

# Constructor to define product attributes
# use underscore to define stock as a private attribute which be modified using a setter method
# getter, setter and deleter must access x with a prepended underscore, which from the outside it is accessed a 
# just with normal name as per class notes

class Product:
    def __init__(self, n:str, l:int, s:int):
        self.__name=n
        self.__lowstockmark=l
        self.__stock=s
    

# Function to print, print all is default parameter when and
# formatting is handled in the print statements
# Printing is done based on single entity in product class, multiple products are handled in shop class
    def print(self):
        print("----------")
        print("Product name is: ", self.__name)
        print("Product low stock mark is: ", self.__lowstockmark)
        print("Stock number is: ", self.__stock)
        print("----------")

# method to get the name of a particular product print it to the screen and also have it returned to the method call
# using return statement
    def get_name(self):
        print 
        print("----------")
        print("Product name is: ", self.__name)
        print("----------")
        return self.__name
        
# using getter, setter and deleter must access x with a prepended underscore, which from the outside it is accessed a just with normal name as per class notes
# have a print statement and a return value to be used by method
    def get_stock(self):
        print("----------")
        print("There are {},  {} units in stock".format(self.__stock, self.__name))
        print("----------")
        return self.__stock

# method to set a stock value for a particular product
# use input to read in an integer
# we are not incrementing by this amount, that is done in shop class. 
# Rather just modifying an existing stock number 
    def set_stock(self):
        new_stock_num=int(input("Please enter a new stock quantity for {} units: ". format(self.__name)))
        print("Current stock quantity is {} ".format(new_stock_num))
        print("New stock quantity is {} ".format(new_stock_num))
        self.__stock = new_stock_num
        print("New set stock value is {}  {} units: ".format(self.__stock, self.__name))

# set a default value for for is_perishable to False, product class is always False. 
# also return the value of False as the default for is_perishable method
# included a print statement and a return value for the is_perishable method
    def is_perishable(self):
        #state=self.is_perishable
        #print(" value is {} : ". format(self.is_perishable()))
        print("----------")
        print("Product {} is Perishable :  ".format(self.__name))
        print("----------")
        return False
    
            
# If current stoick value is less than oir equal to lowstockmark return a True boolean value for stock_is_low() method
# else return a False boolean state
# included print statement as well as a return value for the method

    def stock_is_low(self):
        if self.__stock <= self.__lowstockmark:
            return True
        #if self.__stock <= self.__lowstockmark:
            # print("----------")
            # print("Stock is Low for Product {}. There are {} stock units remaining. Low Stock Mark is {} units".format(self.__name, self.__stock, self.__lowstockmark))
            # print("----------")
            #return True
        else:
            # print("----------")
            # print("Stock is not low for Product {}. There are {} stock units remaining.".format(self.__name, self.__stock))
            # print("----------")
            return False
  
# creating class FoodProduct which is a sub class of of Product 
# adding attribute for use by date which consist of year, month, date(y,m,d)
# specifying default values of None as per spec
# then if y, m and d are true(i.e. not none as per the default, add those values to __useByDate)

class FoodProduct(Product):
    def __init__(self, n, l, s, y=None, m=None, d=None):
        super().__init__(n, l, s)
        if y and m and d:
            self.__useByDate = datetime(y, m, d)
        
        # adding print statement to verify successful creation of Food Product object for end user
        print("----------")
        print("You have successfully added Food Product objects with an expiry date of {}".format(self.__useByDate))
        print("----------")
  
# included a print statement and a return value for is_perishable method
# If ir_perishable is True i.e. it contains y, m and d values, therefore it is not False
# return the value True when y, m and d contain values.
# included Print statement that will only appear if True and also the return value for the method
    def is_perishable(self):
        if self.__useByDate:
            print("----------")
            print("Product is perishable : True")
            print("----------")
            return True
    
# will return True if the useByDate is less than today function in datetime
    def is_out_of_date(self):
        # if useByDate is less than todays date method will return True for is_out_of_date method
        return self.__useByDate < datetime.today()
        
        