import random

print (random.random())

''' Rounding 0-100 '''

print (int(random.random()*100))

''' Simulating a dice roll '''

print (random.randint(1,6))

''' Applying Random to Expected Goals '''

HomexG = [0.21,0.66,0.1,0.14,0.01]
AwayxG = [0.04,0.06,0.01,0.04,0.06,0.12,0.01,0.06]

if random.random()<=0.21:
    print("GOAL!")
else:
    print("Missed!")

# Running the shot count 10,000 times:

Goals = 0

for i in range(0,10000):
    if random.random()<=0.21:
        Goals += 1

print(Goals)

''' Simulating a Match with Expected Goals '''

def calculateWinner(home, away):
    # The match starts at 0-0
    HomeGoals = 0
    AwayGoals = 0
    
    # We have a function within our function
    # This one runs the '.random()' test above for a list
    def testShots(shots):
        
        # Start goal count at 0
        Goals = 0
        
        # For each shot, if it goes in, add a goal
        for shot in shots:
            if random.random() <= shot:
                Goals += 1
                
        # Finally, return the number of goals
        return Goals
    
    # Run the above formula for home and away lists
    HomeGoals = testShots(home)
    AwayGoals = testShots(away)
    
    # Return the score
    if HomeGoals > AwayGoals:
        # print("Home Wins! {} - {}".format(HomeGoals, AwayGoals))
        return("home")
    elif AwayGoals > HomeGoals:
        # print("Away Wins! {} - {}".format(HomeGoals, AwayGoals))
        return("away")
    else:
        # print("Share of the points! {} - {}".format(HomeGoals, AwayGoals))
        return("draw")

# calculateWinner(HomexG, AwayxG)

# Run the xG calculator 10000 times to test winner %
def calculateChance(team1, team2):
    home = 0;
    away = 0;
    draw = 0;
    
    for i in range(0,10000):
        matchWinner = calculateWinner(team1,team2)
        if matchWinner == "home":
            home +=1
        elif matchWinner == "away":
            away +=1
        else:
            draw +=1
    
    home = home/100
    away = away/100
    draw = draw/100
    
    print("Over 10,000 games, home wins {}%, away wins {}% and there is a draw in {}% of games.".format(home, away, draw))

HomexG=[0.5]
AwayxG=[0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05]

calculateChance(HomexG, AwayxG)