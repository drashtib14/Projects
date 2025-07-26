from sys import exc_info
from application_module import *

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