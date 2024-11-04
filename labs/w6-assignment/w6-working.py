class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        # Do not initialize _perishable here

    def set_and_check_perishable(self, perishable):
        """Sets whether the product is perishable and prints its status."""
        self._perishable = perishable  # Set the perishable status

        # Print the current status based on the value of _perishable
        if self._perishable:
            print(f"{self.name} is perishable.")
        else:
            print(f"{self.name} is not perishable.")
        
        return self._perishable  # Return the current status

    def is_perishable(self):
        """Returns whether the product is perishable, or None if not set."""
        if hasattr(self, '_perishable'):
            return self._perishable
        return None  # Or you could raise an error or return a default value

    def __repr__(self):
        return (f"Product(name='{self.name}', price={self.price}, "
                f"perishable={self.is_perishable()})")


# Example usage
milk = Product("Milk", 3.5)  # Create a product without setting perishable
milk_status = milk.set_and_check_perishable(True)  # Set and check perishable status

bread = Product("Bread", 2.0)  # Another product
bread_status = bread.set_and_check_perishable(False)  # Set and check perishable status

# Using __repr__ to see product details
print(milk)  # Outputs: Product(name='Milk', price=3.5, perishable=True)
print(bread) # Outputs: Product(name='Bread', price=2.0, perishable=False)

# Attempt to check perishable status before setting
empty_product = Product("Unknown", 1.0)
print(empty_product.is_perishable())  # Outputs: None
