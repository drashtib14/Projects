import datetime
import os

class Menu:
    def __init__(self):
        self.pizza_price = 10.99
        self.pasta_price = 9.5

    def calculate_pizza_price(self, quantity):
        if quantity == 2:
            return 20.99
        elif quantity == 3:
            return 29.99
        return quantity * self.pizza_price

    def calculate_pasta_price(self, quantity):
        if quantity == 2:
            return 17.00
        elif quantity == 3:
            return 27.50
        return quantity * self.pasta_price

class Customer:
    def __init__(self, name, menu):
        self.name = name
        self.pizza_qty = 0
        self.pasta_qty = 0
        self.total_amount = 0
        self.free_items = []
        self.menu = menu

    def order_pizza(self, quantity):
        self.pizza_qty = quantity
        self.total_amount += self.menu.calculate_pizza_price(quantity)

    def order_pasta(self, quantity):
        self.pasta_qty = quantity
        self.total_amount += self.menu.calculate_pasta_price(quantity)

    def check_free_items(self):
        if self.pizza_qty >= 4:
            self.free_items.append("1.5L Soft Drink")
        if self.pasta_qty >= 4:
            self.free_items.append("2 Bruschetta")
        if self.pizza_qty >= 4 and self.pasta_qty >= 4:
            self.free_items.append("2 Chocco Brownies Ice Cream")

    def print_order_summary(self):
        self.check_free_items()
        print(f"\n\tWelcome, {self.name}")
        print(f"\n\tYour pizza order amount is: {self.menu.calculate_pizza_price(self.pizza_qty):.2f}")
        if self.pizza_qty >= 4:
            print("\t*** Congratulations !! 1.5lt softdrink free ***")

        print(f"\n\tYour pasta order amount is: {self.menu.calculate_pasta_price(self.pasta_qty):.2f}")
        if self.pasta_qty >= 4:
            print("\t*** Congratulations !! get 2 bruschetta free ***")

        if self.pizza_qty >= 4 and self.pasta_qty >= 4:
            print("\t*** Congratulations !! get 2 chocco brownies ice cream free ***")

        print(f"\n\tYour total order is: {self.total_amount:.2f}\n")

class Pizzeria:
    def __init__(self):
        self.menu = Menu()
        self.filename = "pizzeria_bill.txt"
        self.load_previous_data()

    def load_previous_data(self):
        """Loads previous order data from the file to maintain cumulative totals."""
        self.total_sales = 0
        self.total_pizzas = 0
        self.total_pastas = 0
        self.total_soft_drinks = 0
        self.total_bruschetta = 0
        self.total_ice_cream = 0

        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                lines = file.readlines()
                try:
                    self.total_sales = float(lines[2].split(": ")[1])
                    self.total_pizzas = int(lines[3].split(": ")[1])
                    self.total_pastas = int(lines[4].split(": ")[1])
                    self.total_soft_drinks = int(lines[5].split(": ")[1])
                    self.total_bruschetta = int(lines[6].split(": ")[1])
                    self.total_ice_cream = int(lines[7].split(": ")[1])
                except (IndexError, ValueError):
                    print("Warning: Previous data file might be corrupted, starting fresh.")

    def take_order(self):
        while True:
            name = input("\nEnter your name: ")
            customer = Customer(name, self.menu)

            pizza_qty = int(input("\nEnter number of pizzas you want: "))
            customer.order_pizza(pizza_qty)
            self.total_pizzas += pizza_qty

            pasta_qty = int(input("\nEnter number of pastas you want: "))
            customer.order_pasta(pasta_qty)
            self.total_pastas += pasta_qty

            customer.print_order_summary()
            self.total_sales += customer.total_amount

            # Updating free items count
            if "1.5L Soft Drink" in customer.free_items:
                self.total_soft_drinks += 1
            if "2 Bruschetta" in customer.free_items:
                self.total_bruschetta += 2
            if "2 Chocco Brownies Ice Cream" in customer.free_items:
                self.total_ice_cream += 2

            another_customer = input("\nWant to enter order from another customer (Y/N)? ").strip().lower()
            if another_customer != 'y':
                break

    def print_summary(self):
        date = datetime.datetime.now().strftime("%Y-%m-%d")

        summary = (
            "\n----------- Pizza and Pasta Bill --------------\n"
            f"\nDate: {date}\n"
            f"\nTotal payment received today: {self.total_sales:.2f}\n"
            f"Total pizzas sold: {self.total_pizzas}\n"
            f"Total pastas sold: {self.total_pastas}\n"
            f"Total 1.5L soft drinks given: {self.total_soft_drinks}\n"
            f"Total bruschetta given: {self.total_bruschetta}\n"
            f"Total chocco brownies ice cream given: {self.total_ice_cream}\n"
            "\nBye Bye!!!\n"
        )

        print(summary)

        # Instead of overwriting, it updates the existing file
        with open(self.filename, "w") as file:
            file.write(summary)

# Running the code
if __name__ == "__main__":
    pizzeria = Pizzeria()
    pizzeria.take_order()
    pizzeria.print_summary()