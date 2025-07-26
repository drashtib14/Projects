# extened code of IPL

import random

ipl_team_list = ["CSK","RCB","RR","GT","KKR"] # creating list

# taking triple quatation so that values are printed as it is and it allows multiple lines
menu = """
                IPL 2025
            TOP 5 IPL TEAMS ARE :
"""

print(menu)

# variable zone (you can define it if you want)
my_team = ""
opp_team = ""
my_team_balls = 0
opp_team_balls = 0
score_list = [0,1,2,4,6,"WICKET","NO BALL","WIDE",1,2,6,4]
my_team_score = 0
opp_team_score = 0
my_team_wicket = 0
opp_team_wicket = 0

for team in ipl_team_list:
    print(team,end=" | ")

print()
my_team = input("Enter your team: ").upper()

opp_team = random.choice(ipl_team_list)

while opp_team == my_team:
    opp_team = random.choice(ipl_team_list)

print(f"MY TEAM : {my_team}")
print(f"OPP. TEAM : {opp_team}")

print("\n--------------------------------\n")
toss_time = input("TOSS TIME : press H for head or T for tails: ").upper()

if toss_time == "H":
    print("Your choice is Head")
else:
    print("Your choice is Tails")

toss_list = ["Head","Tails"]

print("\n--------------------------------\n")

actual_toss = random.choice(toss_list)

if toss_time == random.choice(toss_list)[0]:
    print("You won the toss!")

    play_menu = """
                        CHOOSE YOUR PLAY SELECTION
                        1) Batting
                        2) Bowling
                        
                        press 1 or 2
            """
    print(play_menu)

    play_selection_choice = int(input("Enter Your Play Selection: "))
    if play_selection_choice == 1:
        print("You have selected bat first")

        # my team bat first
        while  my_team_balls < 6 and my_team_wicket == 0:
            score = random.choice(score_list)
            if score in [0,1,2,4,6]:
                my_team_balls += 1
                my_team_score += score
                print(f"It's {score} run in Over : (0.{my_team_balls})")
                print()
                print(f"{my_team} score is {my_team_score}/{my_team_wicket} Overs (0.{my_team_balls})")
            elif score == "WICKET":
                my_team_wicket += 1
                my_team_balls += 1
                print()
                print(f"It's a wicket")
                print(f"{my_team} score is {my_team_score}/{my_team_wicket} Overs (0.{my_team_balls})")
            elif score in ["NO BALL", "WIDE"]:
                my_team_score += 1
                print()
                print(f"It's a {score}")
                print(f"{my_team} score is {my_team_score}/{my_team_wicket} Overs (0.{my_team_balls})")
            input() # on the enter key next loop will iterate
    else:
        print("You have selected field first")
else:
    print(f"{opp_team} won the toss!")

    play_selection_list = ["bat", "field"]
    opp_play_selection_choice = random.choice(play_selection_list)
    print(f"{opp_team} choose {opp_play_selection_choice} first")