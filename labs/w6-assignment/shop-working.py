# '''
# Week 6 - Assignment -
# Class Inheritance - 3 of 3 files

# --shop.py--
# -eamonn kelly
# '''
from product import Product, FoodProduct

#define variables
divider_line="----------------------------------------"
website_header="Groceries at your Fingertips"
stock_column_headers = ['ID', 'Low Stock Mark', 'Stock']
out_of_stock="Out of Stock"
stock_mgmt_option_menu="Stock Management Options"#
items_in_stock="Items in Stock"


class Shop:
    
    def __init__(self, sp):
        self.shopprods=[]
        print("test1")
        self.shopprods = list(map(lambda prod: Product(prod[0], prod[1], prod[2]) \
            if len(prod) < 4 else FoodProduct(prod[0], prod[1], prod[2], prod[3], prod[4], prod[5]), sp))
        #self.shopproducts = list(map(lambda proditem: Product(proditem[0], proditem[1], None) if len(proditem) < 4 else FoodProduct(proditem[0], proditem[1], proditem[3], None), data))
        #list(map(lambda proditem: Product(*proditem[:3]), FoodProduct(*proditem[3:]), data))
        print("You have successfully added data to shop constructor: ")
        print("test2")
        # print(self.shopprods)
        
        # for sublist in self.shopprods:
        #     for products in sublist:
        #         #name = Product.name
        #         print("prod name {}".format(Product.name))
        # print(self.shopproducts)
        # print("test3")

    def __str__(self):
        return f"Product: {self.name}, lowstockmark: ${self.lowstockmark:.2f}, stock: {self._stock}"


# used isinstance to check for items which are Product and Food Product Objects in the shop prod list. 
# Trioed to use len but len is nor a defined method in the classes, so chose this as adding it was not in spec.
# Do additional logic checks to differentiate between the two classes Products and Food Products, 
    def print_shop(self):     
        print('{:<40}'.format(divider_line) + '\n'
                + '{:^40}'.format(website_header)  + '\n'
                    + '{:<40}'.format(divider_line) + '\n')


        print(items_in_stock + '\n' + '{:<40}'.format(divider_line) + '\n')
        print('{:<5}'.format(stock_column_headers[0])
                + '{:<20}'.format(stock_column_headers[1])
                    + '{:<50}'.format(stock_column_headers[2]))
      
        if not self.shopprods:
            print("There are no products in listed in your shop: ")
        # else:
        #     for product, FoodProduct in self.shopprods:
        #         print("tis prod name{}".format({product.name} ))
            print("test1111")     
        #print(self.shopprods)
            print("test2222")
            global indexed_shopprod_list
            indexed_shopprod_list=[]
        for index, items in list(enumerate(self.shopprods, start=1)):
            indexed_shopprod_list.append([index] + items)    
              
  for items in self.shopprods:
            if isinstance (items, Product)and not isinstance(items, FoodProduct):
                    print('{:<4}'.format(str(groc_item[0])),
                            '{:<9}'.format(str(groc_item[1])),
                                '{:<49}'.format(str(groc_item[2])),
        #         #print("---------------Products----------------")
        #         print(f"Name: {items.name}")
        #         print(f"Low Stock Mark is : {items.lowstockmark}")
        #         print(f"Stock value : {items._stock}")
        #         print("------------------------------")
        # for items in self.shopprods:
        #     if isinstance (items, FoodProduct): 
        #         print("---------------Food Products----------------")
        #         print(f"Name: {items.name}")
        #         print(f"Name: {items.lowstockmark}")
        #         print(f"Stock value : {items._stock}")
        #         print(f"Use By Date: {items.useByDate}")
        #         print("------------------------------")
       
        #             print(items)
        # for items in self.shopprods:
        #     if isinstance (items, FoodProduct) and not isinstance(items, Product):
        #         print("testhhh")
        #         print(items)
# """             """ for item in self.shopprods:
#                 print("2222222")
#                 #is_list = isinstance (item, list)
#                 #print(is_list)
#                 print("22bbb")
#                 print("---------------Products----------------")
#                 print(f"Name: {item.name}")
#                 print(f"Low Stock Mark is : {item.lowstockmark}")
#                 print(f"Stock value : {item._stock}")
#                 #print(f"Stock value : {item.useByDate}")
#                 print("-------------------------------")
#                 # elif len(item) > 4: """ """
                #     print("-------------Food Products----------------")
                #     print(f"Name: {item.name}")
                #     print(f"Low Stock Mark is : {item.lowstockmark}")
                #     print(f"Stock value : {item._stock}")
                #     print(f"UseByDate: {item.useByDate}")
                #     print("-------------------------------")
        
        print("test33333")
            #print(f" low stock mark: {Product}"
            #    self.shopprods(Product.name, Product.lowstockmark, Product._stock))
            #for items in self.shopprods:
            #    print("printing prods {}".format(self.shopprods))
               #for product in self.products:  
              #  if isinstance(Product, FoodProduct):
                #print(f"FoodProduct: Product: {Product.name}")
                #print(self.shopprods)
            #               f"Description: {product.description}, Expiry Date: {product.expiry_day:02d}-{product.expiry_month:02d}-{product.expiry_year}")
            #     else:
            #         print(f"Product: {product.name}, Price: ${product.price:.2f}, Description: {product.description}")
          
            
            
            # for product in self.shopproducts:
            #     print(f"Name: {product.name}")
            #     print(f"Low Stock value: {product.lowstockmark}")
            #     print(f"Stock: {product.lowstockmark}")
            #     print(f "name: {FoodProduct.is_perishable}"")
            #     print("---------")
#prod=lambda proditem: Product(*proditem[:2], FoodProduct(*proditem[3:-1]), data))
#print DATA [:2]

#products = list(map(lambda proditem: Product(proditem[0], proditem[1], None) if len(proditem) < 4 else FoodProduct(proditem[0], proditem[1], proditem[3], None), DATA))