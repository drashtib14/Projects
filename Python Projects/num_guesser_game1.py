# the code works fine but it gives NameError at runtime for user2 and user3 (tried defining it with None value but doesn't work) but still it works all fine
# import num_guesser_game2 # here's the code without error

"""
Game: Guess a number and check whether did computer choose this number or not.
Conditions:
There will be 3 rounds in total.
user will have 5 chance to find out correct number in first 2 rounds and in the last round user will have 4 chances only.
number will be guessed between 1-100 in the 1st round,
1-150 in 2st round,
1-200 in 3st round
"""

import random # import random module

computer = random.randint(1,100) # comp guessing

for i in range(1,6): # loop to iterate 5 times
    user = int(input("Enter Your choice (between 1-100): ")) # taking number from user

    if user > computer: # if user guessed number is bigger than comp then following statement will print
        print("HINT: Guess lower number")
    elif user < computer: # if user guessed number is smaller than comp then following statement will print
        print("HINT: Guess upper number")
    elif user == computer:  # if user guessed number is same as comp then following statement will print
        print("\n********* YOU WON THE 1ST ROUND! *********")
        break # break will stop loop once user have won
    else:
        pass # no values to be applied in else part
        
if user != computer:
        print("\nYou lose the Game. The correct number was ",computer)

if user == computer:
    print("\nYou've entered 2nd round!")
    computer2 = random.randint(1,150) # comp guessing
    user2 = None

    for i in range(1,6): # loop to iterate 5 times
        user2 = int(input("Enter Your choice (between 1-150): "))

        if user2 > computer2: # if user guessed number is bigger than comp then following statement will print
            print("HINT: Guess lower number")
        elif user2 < computer2:  # if user guessed number is smaller than comp then following statement will print
            print("HINT: Guess upper number")
        elif user2 == computer2: # if user guessed number is same as comp then following statement will print
            print("\n********* YOU WON THE 2ST ROUND! *********")
            break
        else:
            pass
        
if user2 != computer2:
        print("\nYou lose the Game. The correct number was ",computer2)

if user2 == computer2:
    print("\nYou've enterd FINAL ROUND")
    computer3 = random.randint(1,200) # comp guessing
    user3 = None

    for i in range(1,5): # loop to iterate 5 times
        user3 = int(input("Enter Your choice (between 1-150): "))

        if user3 > computer3: # if user guessed number is bigger than comp then following statement will print
            print("HINT: Guess lower number")
        elif user3 < computer3: # if user guessed number is smaller than comp then following statement will print
            print("HINT: Guess upper number")
        elif user3 == computer3: # if user guessed number is same as comp then following statement will print
            print("\n********* YOU WON THE FINAL ROUND! *********\n")
            break
        else:
            pass

if user3 != computer3:
        print("\nYou lose the Final round. The correct number was ",computer3)