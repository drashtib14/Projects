print("------KALYAN JWELLERS------\n")

# getting input from user
name = input("Enter Your Name: ")
gender = input("Enter Your gender (M/F): ")    
age = int(input("Enter Your Age: "))
product = input("Enter Product: ")
product_grm = int(input("Enter product gram: "))

print("-------------------------------------------------------------------\n")

# calculation
gold_price = 5752  # 1 gram
print(f"Current Gold Price: {gold_price}")

total_gold = product_grm * gold_price
print(f"Total Gold Rate: {total_gold}")

charges = 845
total_charges = product_grm * charges
print(f"After making charges: {total_charges}")

total_amount = total_gold + total_charges
print(f"Total Amount: {total_amount}")

# discount
discount = 0

# Male discount logic
if gender == 'M' or gender == 'm':
    if age >= 65:
        if total_gold >= 200000 and total_gold < 300000:
            discount = 0.20
        elif total_gold >= 300000 and total_gold < 500000:
            discount = 0.30
        elif total_gold >= 500000:
            discount = 0.35
else:  # age < 65
    if total_gold >= 200000 and total_gold < 300000:
        discount = 0.10
    elif total_gold >= 300000 and total_gold < 500000:
        discount = 0.20
    elif total_gold >= 500000:
        discount = 0.25

# Female discount logic
if gender == 'F' or gender == 'f':
    if age >= 65:
        if total_gold >= 200000 and total_gold < 300000:
            discount = 0.25
        elif total_gold >= 300000 and total_gold < 500000:
            discount = 0.35
        elif total_gold >= 500000:
            discount = 0.40
else:  # age < 65
    if total_gold >= 200000 and total_gold < 300000:
        discount = 0.15
    elif total_gold >= 300000 and total_gold < 500000:
        discount = 0.25
    elif total_gold >= 500000:
        discount = 0.30

# printing values/output
print("-------------------------------------------------------------------\n")
discount_amount = total_gold * discount
print(f"Discount Applied: ₹{discount_amount}")

net_total = total_amount - discount_amount
print(f"Total Net Amount: ₹{net_total}\n")