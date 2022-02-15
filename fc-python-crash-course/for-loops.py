TeamA = ["Nasta","Overvenus","Ranalda"]

for player in TeamA:
    print("Welcome to the cage, " + player)

#Team 2, enter!
TeamB = ["Tatti","Nikita","Hanry"]

#A list of lists!
Teams = [TeamA,TeamB]

for team in Teams:
    for player in team:
        print("Welcome to the cage, " + player)