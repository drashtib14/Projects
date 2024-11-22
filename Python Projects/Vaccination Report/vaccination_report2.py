# only reports of the same day. when the it's the next day new file should be created.
# This program writes header only one time after creating the file.

# import datetime
from datetime import datetime
from os import path

# Get current date and time
x = datetime.now() # to find current datetime
cdate = x.strftime("%d%m%Y") # current date
ctime = x.strftime("%H:%M:%S") # current time

# Vaccination report header
header = """
                VACCINATION REPORT 
===================================================
"""

# Vaccination report current data and time
current_dt = f"""
---------------------------------------------------
Date:  {cdate}           Time:  {ctime}
---------------------------------------------------
"""

# taking user input
name = input("Enter your name: ")
email = input("Enter your email: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender: ")
vaccine = input("Enter your vaccine: ")
vaccine_dose = input("Enter your vaccine Dose: ")

# Generating a filename for the report based on the current date
filename = f"Vaccination_Report_{cdate}.txt"

# if the header exists in file then dont rewrite it
header_exists = False
if path.exists(filename):
    with open(filename, "r") as f:
        header_exists = header in f.read()

# if it doesn't exist then write
with open(filename, "a") as f:
    if not header_exists:
        f.write(header)

with open(filename,"a") as f:
    f.write(current_dt)
    f.write(f"Name: {name} \nEmail: {email} \nAge: {age} \nGender: {gender} \nVaccine: {vaccine} \nVaccine Dose: {vaccine_dose}")
    f.write("\n===================================================")

# final message to the user
print(f"\nVaccination report has been saved as '{filename}'")