from sys import exc_info
import json
from application_module import *

# Load fruit stock and customer data at the start
loadFruitStock()
loadCustomerData()

while True:
    try:
        roleInput() # main code
    except ValueError:
        print("Please Enter Numbers Only")
        continue # to take input from user again 
    # except Exception:
        print("Something went wrong")
        # to know which error occured
        # print(f"Error Type: {exc_info()[0]}")
        # print(f"Error Message: {exc_info()[1]}")
        break
    finally:
        print("Thank You for using Our Application")