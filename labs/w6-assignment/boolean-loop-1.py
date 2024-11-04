class MyClass:
    def my_method(self, my_variable=""):
        if my_variable:
            print("Variable is populated:", my_variable)
        else:
            print("Variable is empty.")
            my_variable = input("Please enter a value to populate the variable: ")
            print("You entered:", my_variable)
            
