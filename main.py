import random

def probMethod():
    thresh = 0.95 
    p = 20.0/((122*123)/2) #Pairs per game / unique pairs
    i = 0
    totalP = 0

    while totalP < thresh:
        totalP = totalP + (p*(1-totalP))
        i = i + 1

    return i

print(probMethod())

def bruteForce():

    remaining = list(range(7500))
    games = 0

    while len(remaining) > 375:
        for i in range(20):
            x = random.randint(0, 7500)
            if x in remaining:   
                remaining.remove(x)
        games = games + 1

    return games

print(bruteForce())

    
