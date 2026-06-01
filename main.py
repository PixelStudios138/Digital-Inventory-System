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
        return f"ID: {self.product_id} | {self.name} (${self.price}) | Stock: {self.quantity}"

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

inventory = Inventory({})

def update_stock():
    print("What do you want to do?")
    print("1) Restock product")
    print("2) Sell product")
    choice = input("Make your choice (1/2): ")
    if choice.int() != 1 or choice.int() != 2:
        print("Incorrect input selected, try again")
        update_stock()
    elif choice == 1:
        product_id = input("What is the id of the product you want to restock?")
        amount = input("How much more do you want to restock it by?")
        inventory.restock(product_id, amount)

if __name__ == "__main__":
    print("Welcome to the inventory")
    print("What would you like to do?")
    print("1) Add new product")
    print("2) View full inventory")
    print("3 Update Product Stock")
    print("4) Exit")