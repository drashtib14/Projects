"""
Game: Guess a number and check whether did computer choose this number or not.
Conditions:
There will be 3 rounds in total.
user will have 5 chances to find out correct number in first 2 rounds and in the last round user will have 4 chances only.
number will be guessed between 1-100 in the 1st round,
1-150 in 2st round,
1-200 in 3st round
"""

import random  # import random module

computer = random.randint(1, 100) # comp guessing

for i in range(1, 6): # loop to iterate 5 times
    user = int(input("Enter Your choice (between 1-100): "))

    if user > computer:
        print("HINT: Guess lower number")
    elif user < computer:
        print("HINT: Guess upper number")
    elif user == computer:
        print("\n********* YOU WON THE 1ST ROUND! *********")
        break

if user != computer:
    print("\nYou lost the 1st round. The correct number was ", computer)
else:
    print("\nYou've entered 2nd round!")
    computer2 = random.randint(1, 150) # comp guessing
    
    for i in range(1, 6): # loop to iterate 5 times
        user2 = int(input("Enter Your choice (between 1-150): "))

        if user2 > computer2:
            print("HINT: Guess lower number")
        elif user2 < computer2:
            print("HINT: Guess upper number")
        elif user2 == computer2:
            print("\n********* YOU WON THE 2ND ROUND! *********")
            break

    if user2 != computer2:
        print("\nYou lost the 2nd round. The correct number was ", computer2)
    else:
        print("\nYou've entered FINAL ROUND!")
        computer3 = random.randint(1, 200) # comp guessing

        for i in range(1, 5): # loop to iterate 5 times
            user3 = int(input("Enter Your choice (between 1-200): "))

            if user3 > computer3:
                print("HINT: Guess lower number")
            elif user3 < computer3:
                print("HINT: Guess upper number")
            elif user3 == computer3:
                print("\n********* YOU WON THE FINAL ROUND! *********\n")
                break

        if user3 != computer3:
            print("\nYou lost the Final round. The correct number was ", computer3)
