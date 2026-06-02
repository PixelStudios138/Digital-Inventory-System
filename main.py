class Product():
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_stock(self, amount):
        self.quantity += amount
        if self.quantity <= 0:
            self.quantity = 0

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
        self.products[product_id].update_stock(amount)

    def sell_product(self, product_id, amount):
        if self.products[product_id].quantity >= amount:
            self.products[product_id].quantity -= amount
        else:
            raise Exception("Sorry, there aren't enough items to sell")

    def display_all(self):
        for product in self.products.values():
            print(product)

inventory = Inventory({})
laptop = Product("001", "Laptop", 699.99, 500)
apple = Product("002", "Apple", 2.50, 1000)
pencil = Product("003", "Pencil", 0.50, 100)
chair = Product("004", "Chair", 15, 300)
guitar = Product("005", "Electric Guitar", 500, 6750)

def update_stock():
    print("What do you want to do?")
    print("1) Restock product")
    print("2) Sell product")
    choice = input("Make your choice (1/2): ")
    if choice == "1":
        product_id = input("What is the id of the product you want to restock? ")
        amount = int(input("How much do you want to restock it by? "))
        inventory.restock(product_id, amount)
    elif choice == "2":
        product_id = input("What is the id of the product you want to sell?")
        amount = int(input("How much do you want to sell it by?"))
        inventory.sell_product(product_id, amount)
    else:
        print("Incorrect input selected, try again")
        update_stock()

def mainLoop():
    print("What would you like to do?")
    print("1) Add new product")
    print("2) View full inventory")
    print("3) Update Product Stock")
    print("4) Exit")
    choice = input("What is your choice (1, 2, 3, 4)? ")
    if choice == "1":
        id = input("What is the id of the product you wish to add? ")
        name = input("What is the name of your product? ")
        price = input("How much does it cost? ")
        quantity = input("How many do you have? ")
        new_product = Product(id, name, price, quantity)
        inventory.add_product(new_product)
    elif choice == "2":
        inventory.display_all()
    elif choice == "3":
        update_stock()
    elif choice == "4":
        quit()
    else:
        print("Invalid option. Try again.")
        mainLoop()

if __name__ == "__main__":
    print("Welcome to the inventory")
    inventory.add_product(laptop)
    inventory.add_product(apple)
    inventory.add_product(pencil)
    inventory.add_product(chair)
    inventory.add_product(guitar)
    while True:
        mainLoop()

