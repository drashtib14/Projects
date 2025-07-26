import json

# Variables
menu = """
            WELCOME TO FRUIT MARKET

            1) Manager
            2) Customer
            0) Enter 0 to Exit
"""

manager_menu = """
            Fruit Market Manager

            1) Add Fruit Stock
            2) View Fruit Stock
            3) Update Fruit Stock
            0) Go Back to Main Manu
"""

customer_menu = """
            1) View Available Fruits
            2) Buy Fruits
            0) Go Back to Main Menu
"""

# Dictionaries
fruit_items = {}
# fruit_details = {}

# Functions

# getting the role of the user. manager or customer
def roleInput():
    print(menu)
    # using while condition so if user enters wrong input, we can get their input again
    role_input = True
    while role_input != False:
        role = int(input("Select Your Role: ")) # getting role to know wether it is manager or customer

        # giving operations according choice of role
        if role == 1:
            print(manager_menu)
            managerOperations()
            role_input = False
        elif role == 2:
            customerOperations()
            role_input = False
        elif role == 0:
            exit()
        else:
            print("Invalid input. Enter 1, 2 or 0")
            role_input = True

# asking manager if they wanna perform more operations
def askContinue():
    # taking user input to ask if they want to perform more operations
    user_input = input("Do you want to perform more operations? Press y for yes and n for no: ").lower()
    if user_input == "y" or user_input == "yes":
        print(manager_menu)
        manager_choice = True
    else:
        manager_choice = False
        roleInput()
    return manager_choice

# display available fruit items to user
def displayStock():
    # printing available stock
    if fruit_items:
        for fruit, details in fruit_items.items():
            print(f"\n{fruit}: \nQuantity = {details['qty']}kg \nPrice = {details['price']} per kg")
    else:
        print("No fruits available in stock currently.")

# for manager choice like add view update
def managerOperations():
    while True:
        try:
            # looping till user enters 1 2 3 or 0
            manager_choice = True
            while manager_choice != False:
                manager_choice = int(input("Enter Your Choice: ")) # getting user choice
                # Add fruit stock
                if manager_choice == 1:
                    print("ADD FRUIT STOCK\n")
                    fruit_name = input("Enter fruit name: ").capitalize()
                    # fruit_details["qty"] = input("Enter quantity (in kg): ")
                    # fruit_details["price"] = input("Enter price: ")
                    # qty = int(input("Enter quantity (in kg): "))
                    # price = int(input("Enter price: "))
                    while True:
                        try:
                            qty = int(input("Enter quantity (in kg): "))
                            price = int(input("Enter price: "))
                            break
                        except ValueError:
                            print("Please Enter Numbers Only")
                            continue

                    # fruit_items[fruit_name] = fruit_details
                    fruit_items[fruit_name] = {"qty": qty, "price": price}
                    print(f"{fruit_name} has been added to stock.\n")
                    managerFile()
                    # taking user input to ask if they want to perform more operations
                    askContinue()
                # View fruit stock
                elif manager_choice == 2:
                    print("VIEW FRUIT STOCK\n")
                    print(fruit_items) # prints dictionary
                    # printing available stock
                    displayStock()
                    # taking user input to ask if they want to perform more operations
                    askContinue()
                # update fruit stock
                elif manager_choice == 3:
                    print("UPDATE FRUIT STOCK\n")
                    fruit_name = input("Enter the name of the fruit to update: ").capitalize()
                    # if fruit exists then asks user to enter input to update value
                    if fruit_name in fruit_items:
                        # qty = input("Enter new quantity (in kg): ")
                        # price = input("Enter new price: ")
                        while True:
                            try:
                                qty = int(input("Enter quantity (in kg): "))
                                price = int(input("Enter price: "))
                                managerFile()
                                break
                            except ValueError:
                                print("Please Enter Numbers Only")
                                continue
                        fruit_items[fruit_name] = {"qty": qty, "price": price}
                        print(f"{fruit_name} has been updated.\n")
                    else:
                        print(f"{fruit_name} is not in stock.\n")
                    # taking user input to ask if they want to perform more operations
                    askContinue()
                elif manager_choice == 0:
                    # back to main menu
                    roleInput()
                else:
                    # this will execute until the user enters 1 2 or 3
                    print("Invalid input. Enter 1, 2, 3 or 0")
                    manager_choice = True
        except ValueError:
            print("Please Enter Numbers Only")
            continue

# customer operations like view and buy prodcuts
def customerOperations():
    global customer_name # to use variable in other functions
    customer_name = input("Enter Your Name: ").capitalize()
    print(f"\nWelcome, {customer_name}!")
    print(customer_menu)
    while True:
        try:
            # looping until user enters 1 2 or 0
            customer_choice = True
            while customer_choice != False:
                customer_choice = int(input("Enter Your Choice: "))

                if customer_choice == 1:
                    # view available fruits
                    displayStock()
                    print()
                    print(customer_menu)
                    customer_choice = True
                elif customer_choice == 2:
                    # buy fruits
                    buyFruits()
                    # taking user input to ask if they want to buy more fruits
                    user_input = input("Do you want to buy more Fruits? Press y for yes and n for no: ").lower()
                    if user_input == "y" or user_input == "yes":
                        buyFruits()
                        customer_choice = True
                        print(customer_menu)
                    else:
                        customer_choice = False
                        print(customer_menu)
                elif customer_choice == 0:
                    print(f"Thank you for visiting, {customer_name}!")
                    # back to main menu
                    roleInput()
                else:
                    print("Invalid input. Please enter 1, 2, or 0")
    
        except ValueError:
            print("Please Enter Numbers Only")

# for customer to buy fruits
def buyFruits():
    fruit_name = input("Enter the Fruit you want to buy: ").capitalize()
            
    # checking if the fruit exists in the dictionary
    if fruit_name in fruit_items:
        available_qty = int(fruit_items[fruit_name]["qty"])
        while True:
            try:
                qty_to_buy = int(input(f"How many kg of {fruit_name} would you like to buy? "))
                break # to exit this infinite loop
            except ValueError:
                print("Please Enter Numbers Only")
                continue
        # if the qty to buy is less then available quantity then purchase
        if qty_to_buy <= available_qty:
            fruit_items[fruit_name]["qty"] = available_qty - qty_to_buy
            print(f"Thank you {customer_name}! You have successfully purchased {qty_to_buy}kg of {fruit_name}.\n")
            managerFile() # saving stock changes into json file
            # customerPurchase(customer_name, fruit_name, qty_to_buy)
            logCustomerPurchase(customer_name, fruit_name, qty_to_buy)  # Log the transaction
        else:
            print(f"Sorry, only {available_qty}kg of {fruit_name} is available.\n")
    else:
        print(f"{fruit_name} is not available in stock\n")


# File handling

# manager
# Save stock changes to a JSON file
def managerFile():
    with open("fruit_stock.json", "w") as f:
        json.dump(fruit_items, f, indent=4)
    print("Changes have been saved to fruit_stock.json")

# item qty will be added to existing qty
def addItem(fruit_name, quantity, price):
    if fruit_name in fruit_items:
        fruit_items[fruit_name]["quantity"] += quantity  # Update quantity if item exists
    else:
        fruit_items[fruit_name] = {"quantity": quantity, "price": price}  # Add new item
    managerFile()  # Save changes to file
    print(f"Added {quantity} of {fruit_name} at ${price} each.")

# replaces old qty and price if they exists
def updateItem(fruit_name, quantity=None, price=None):
    if fruit_name in fruit_items:
        if quantity is not None:
            fruit_items[fruit_name]["quantity"] = quantity  # Update quantity
        if price is not None:
            fruit_items[fruit_name]["price"] = price  # Update price
        managerFile()  # Save changes to file
        print(f"Updated {fruit_name}: Quantity = {quantity}, Price = {price}.")
    else:
        print(f"{fruit_name} does not exist in stock.")

# to access json file (all items saved in file) when starting the program
def loadFruitStock():
    global fruit_items # using global so it can be used outside the function
    try:
        with open("fruit_stock.json", "r") as f:
            fruit_items = json.load(f)
            # print("Stock loaded successfully.")
    except FileNotFoundError:
        print("No previous stock found. Starting with an empty stock.")
    except json.JSONDecodeError:
        print("Error reading the stock file. Starting with an empty stock.")


# customer

customer_data = {}

# Load customer data from JSON file at startup
def loadCustomerData():
    global customer_data
    try:
        with open("customer_data.json", "r") as f:
            customer_data = json.load(f)
    except FileNotFoundError:
        print("No customer data found. Starting fresh.")
    except json.JSONDecodeError:
        print("Error reading customer data. Starting fresh.")

# Save customer transaction
def logCustomerPurchase(customer_name, fruit_name, qty_to_buy):
    import datetime
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Add customer data
    if customer_name not in customer_data:
        customer_data[customer_name] = []
    
    # Append the purchase record
    customer_data[customer_name].append({
        "fruit": fruit_name,
        "quantity": qty_to_buy,
        "timestamp": timestamp
    })
    
    # Save to JSON file
    with open("customer_data.json", "w") as f:
        json.dump(customer_data, f, indent=4)
    
    print(f"Purchase of {qty_to_buy}kg {fruit_name} by {customer_name} logged successfully.")