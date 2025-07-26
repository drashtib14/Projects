# Objective: Determine the user's fitness status based on their exercise routine

# getting number from user
num = int(input("Enter the number of minutes you exercise per week: "))

# setting conditions
if num > 0 and num <= 59 :
    print("Your fitness level is: Sedentary\n")
elif num >= 60 and num <= 149 :
    print("Your fitness level is: Moderately Active\n")
elif num >= 150 and num <= 299 :
    print("Your fitness level is: Active\n")
elif num >= 300 :
    print("Your fitness level is: Very Active\n")
else :
    print("Invalid input\n")