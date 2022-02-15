''' Comparison Operators '''

# Is four greater than three?
print (4 > 3)

# Is four less than three?
print (4 < 3)

# Is 20 less than or equal to 21?
print (20 <= 21)

# Does 44 equal 44? We use 2 equals signs here!
print (44 == 44)

# Our skill ranking system assigns two players a ranking, Who is better?

Garrerd = 99
Landard = 98

print (Garrerd > Landard)

''' Logic Operators '''

# Garrerd = 99 and Landard = 98 as in the last example
# Check that Garrerd is better AND that can we afford them?

Budget = 5000000
PlayerCost = 4000000

print ((Garrerd > Landard) and (Budget >= PlayerCost))

HerderGoals = 9
HerderAssists = 16

print ((HerderGoals > 10) or (HerderAssists >= 15))

MertaGoals = 5
MertaAssists = 10
MertaRedCards = 3

print ((MertaGoals > 5) or ((MertaAssists>=5) and (MertaRedCards<3)))