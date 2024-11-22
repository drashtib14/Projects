"""
playing rock paper scissor with computer.
this code takes string in input
"""
import random # import random module

game_options = ["ROCK","PAPER","SCISSOR"] # creating list which contains 3 elements

status = True
while status :
    print("\nEnter 1 for ROCK \nEnter 2 for PAPER \nEnter 3 for SCISSOR\n")
    user_choice = int(input("Enter Your Choice: ")) # taking user's choice
    computer = random.choice(game_options) # computer will randomly pick from game_options and it is saved in computer variable

    # condition to print string instead of numbers of user's choice
    if user_choice == 1:
        user_choice = "ROCK"
        print("User's choice: ROCK") # displaying user's choice
    elif user_choice == 2:
        user_choice = "PAPER"
        print("User's choice: PAPER") # displaying user's choice
    elif user_choice == 3:
        user_choice = "SCISSOR"
        print("User's choice: SCISSOR") # displaying user's choice
    else:
        print("Invalid value, please enter 1, 2, or 3")
        continue
        
    print("Computer's choice: ",computer) # displaying computer's choice

    # conditions to decide who wins the game
    if (user_choice == "ROCK" and computer == "PAPER") or (user_choice == "PAPER" and computer == "SCISSOR") or (user_choice == "SCISSOR" and computer == "ROCK"):
        print("******** COMPUTER WON THE GAME ********")
    elif (user_choice == "PAPER" and computer == "ROCK") or (user_choice == "SCISSOR" and computer == "PAPER") or (user_choice == "ROCK" and computer == "SCISSOR"):
        print("******** USER WON THE GAME ********")
    else:
        print("******** TIE ********")

    repeat = input("Do you want to play again? Enter y or n: ").lower() # asking to user whether they wanna play again or not (in the loop)
    if repeat == 'y': # if user enter's y then condition is true. it will return the status true and while loop will be executed again
        status = True
    else: # else status will be false and it will cause the loop to terminate
        status = False