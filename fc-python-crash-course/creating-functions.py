def doubleMe(number):
    return number*2
    
print(doubleMe(2))

''' Create a function that generates a tweet. '''

def newTweet(player, action, success):
    tweet = player + " plays a " + action + "."
    if (success):
        if action == "pass":
            tweet += " The team keep possession"
        elif action == "shot":
            tweet += " GOOOOOAAAAAAALLLLLL"
    else:
        if action == "pass":
            tweet += " The pass is unsuccessful"
        elif action == "shot":
            tweet += " No goal this time!"
            
    return tweet
    
print(newTweet("Pearlo", "shot", True))