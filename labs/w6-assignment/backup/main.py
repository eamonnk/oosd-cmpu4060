from product import Product, FoodProduct
from shop import Shop


DATA = [
    ["teapot", 5, 4],
    ["table", 5, 8],
    ["bed", 3, 5],
    ["milk", 3, 1, 2024, 11,21],
    ["bread", 3, 4, 2024, 11,4],
    ["tea", 3, 12, 2024, 11,7],
    ["cake", 3, 12, 2024, 11, 6],
]
DATA1 = []

# Uncomment individual lines in a secion and run them to test
# Re-comment the section when complete and move ot the next section and repeat
# ---- Scenraio 1 - Testing product class ----------
# ---- Add product to product class, print the product object---
p1=Product("teapot", 5, 4)
p1.print()
p1.get_name()
#myshop=Shop(DATA)
#myshop.print_product_list("od")
#print(myshop.name)
#myshop.is_out_of_stock()
#p1.get_name()
#p1.set_stock()
#p1.print()
#p1.is_perishable()
#p1.stock_is_low() 
#p1.print.stock_is_low()

# shopprods=[]
# print("test1")
# #shopprods = list(map(lambda Data :(DATA[0], DATA[1], DATA[2]), DATA ))

# new_list = list(map(lambda x: x, DATA))
#         #             \
#         # if len(proditem) < 4 else FoodProduct(proditem[0], proditem[1], proditem[2], proditem[3], proditem[4], proditem[5]), data))
#         #self.shopproducts = list(map(lambda proditem: Product(proditem[0], proditem[1], None) if len(proditem) < 4 else FoodProduct(proditem[0], proditem[1], proditem[3], None), data))
#         #list(map(lambda proditem: Product(*proditem[:3]), FoodProduct(*proditem[3:]), data))
# print("You have successfully added data to shop constructor: ")
# print("test2")
# print(shopprods)
# print("test3")
# print(new_list)
# print("test4")
# print(new_list[0][2])