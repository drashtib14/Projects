import random

ipl_team_list = ["CSK","RCB","RR","GT","KKR"] # creating list

# taking triple quatation so that values are printed as it is and it allows multiple lines
menu = """
                IPL 2025
            TOP 5 IPL TEAMS ARE :
"""

print(menu)

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

# actual_toss = random.choice(toss_list) # you can also do this way

if toss_time == random.choice(toss_list)[0]:
    print("You won the toss!")
else:
    print(f"{opp_team} won the toss!")