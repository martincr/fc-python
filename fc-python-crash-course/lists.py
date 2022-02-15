GF = [0,0,3,2,1,5,3,1,2]
GA = [2,0,2,2,3,2,3,2,4]

print(GF)
print(GA)

print(GF[0])
print(GA[0])

print ("Goal difference " + str(GF[0] - GA[0]))

P = 0
GD = 0
GF = [0,0,3,2,1,5,3,1,2]
GA = [2,0,2,2,3,2,3,2,4]

#We have 9 games, so we iterate with a range of 9 in a for loop
for i in range(9):
    #If we score more, give us 3 points and add the goal difference
    if GF[i] > GA[i]:
        P += 3
        GD += (GF[i] - GA[i])
    #If we draw, give us a point. Goal difference will stay the same.
    elif GF[i] == GA[i]:
        P += 1
    #If we lose, we get no points, but update the goal difference
    else:
        GD += (GF[i] - GA[i])

print(P)
print(GD)

''' Range '''

#One argument in range()
#Give me the list of 10 numbers, starting at 0
print (list(range(10)))

#Two arguments in range()
#Give me all numbers between these two
print (list(range(5,10)))

#Three arguments in range()
#Give me all numbers between the first two, in steps of the third number
print (list(range(0,10,2)))

''' Selecting a number from a list '''

Players = ["Didek","Bascin","Smacer","Boras","Finnon"]

#Select the 4th player - remember that the count starts at 0!
print(Players[3])

#Select the middle 3 players (Bascin, Smacer and Boras)
print(Players[1:4])

''' List Methods '''

GF = [0,0,3,2,1,5,3,1,2]
GA = [2,0,2,2,3,2,3,2,4]

#Let's add a new score to our goals for and goals against lists
#The append() method will help us here

GF.append(3)
GA.append(1)

#Show the scores, 3-1 should be the final column
print(GF)
print(GA)

GF = [0, 0, 3, 2, 1, 5, 3, 1, 2, 3]
GA = [2, 0, 2, 2, 3, 2, 3, 2, 4, 1]

#I want to reverse the scores, to see the 5 most recent ones
#Reverse() will make this light work

GF.reverse()
GA.reverse()
print(GF[0:5])
print(GA[0:5])