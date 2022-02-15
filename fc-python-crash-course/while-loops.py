watchMinutes = 0

while watchMinutes < 45:
    watchMinutes += 1

print(str(watchMinutes) + " played, it is half-time!")

import random

keepPossession = True
passSkill = 66
passesComplete = 0

while keepPossession == True:
    
    if random.randint(0,100) > passSkill:
        keepPossession = False
    else:
        passesComplete += 1
        
print(passesComplete)