class Product():
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_stock(self, amount):
        quantity += amount
        if quantity <= 0:
            quantity = 0
        self.quantity = quantity

    def get_total_value(self):
        total_value = self.quantity * self.price
        return total_value

    #function that gets called if a print statement is called
    #if the program encounters a line like print(Product), this method will be called
    def __str__(self):
        return f"ID: {self.product_id} | {self.name} ({self.price}) | Stock: {self.quantity}"

class Inventory():
    def __init__(self, products):
        self.products = products

    def add_product(self, product):
        self.products[product.product_id] = product

    def restock(self, product_id, amount):
        self.products[product_id].quantity += amount

    def sell_product(self, product_id, amount):
        if self.products[product_id].quantity >= amount:
            self.products[product_id].quantity -= amount
        else:
            raise Exception("Sorry, there aren't enough items to sell")

    def display_all(self):
        for product in self.products.values():
            print(product)

laptop = Product("203", "Laptop", 1030.98, 20)    
apple = Product("001", "Apple", 5.99, 30)
inventory = Inventory({})
inventory.add_product(laptop)
inventory.add_product(apple)
inventory.restock("203", 589)
inventory.sell_product("203", 300)
inventory.display_all()