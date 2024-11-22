# create a program to determine the price of a movie ticket based on the user's age and the day of the week

# taking input from user
age = int(input("Enter Your Age: "))
day = input("Enter the day of the week: ").lower()

if age > 0 and age <= 12 : # for children 0-12
    base_price = 5
    if day == "saturday" or day == "sunday" :
        discount = base_price / 100 * 10
        final_price = base_price - discount
    else :
        discount = 0.00
        final_price = base_price
elif age > 12 and age <= 17 : # for teenagers 13-17
    base_price = 8
    if day == "saturday" or day == "sunday" :
        discount = base_price / 100 * 10
        final_price = base_price - discount
    else :
        discount = 0.00
        final_price = base_price
elif age > 17 and age <= 64 : # for adults 18-64
    base_price = 12
    if day == "saturday" or day == "sunday" :
        discount = base_price / 100 * 10
        final_price = base_price - discount
    else :
        discount = 0.00
        final_price = base_price
elif age > 64 : # for children 65 and above
    base_price = 7
    if day == "saturday" or day == "sunday" :
        discount = base_price / 100 * 10
        final_price = base_price - discount
    else :
        discount = 0.00
        final_price = base_price
else :
    print("Invalid input")

# printing values 
print(f"\nBase Price: ${base_price:.2f}")
print(f"Discount: ${discount:.2f}")
print(f"Final Price: ${final_price:.2f}\n")