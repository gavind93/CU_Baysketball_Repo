import random
import numpy as np

def winProbability(teamSeed, opponentSeed):
    if(teamSeed < 1 or teamSeed > 16 or type(teamSeed)!=int):
        print ('Please enter valid seed for teamSeed')
        return -1
    if(opponentSeed < 1 or opponentSeed > 16 or type(opponentSeed)!=int):
            print ('Please enter valid seed for opponentSeed')
            return -1
    seedSum= opponentSeed + teamSeed
    winProb = opponentSeed/seedSum
    return winProb

def first_round():
    regions = np.empty((4,8))
    for i in range(4):
        results = np.empty(8)
        for j in range(8):
            if(winProbability(j+1,16-j) > random.uniform(0,1)):
                results[j] = int(j+1)
            
            else:
                results[j] = int(16-j)
            
        regions[i] = results
    return regions



def second_round(first_results):
    regions = np.empty((4,4))
    for i in range(4):
        second_results = np.empty(4)
        for j in range(4):
            if(winProbability(int(first_results[i][j]),int(first_results[i][7-j])) > random.uniform(0,1)):
                second_results[j] = first_results[i][j]
                 
            else:
                second_results[j] = first_results[i][7-j]
                 
        regions[i] = second_results
    return regions

def sweet_16(second_results):
    regions = np.empty((4,2))
    for i in range(4):
        sweet_results = np.empty(2)
        for j in range(2):
            if(winProbability(int(second_results[i][j]),int(second_results[i][3-j])) > random.uniform(0,1)):
                sweet_results[j] = second_results[i][j]
                 
            else:
                sweet_results[j] = second_results[i][3-j]
                 
        regions[i] = sweet_results
    return regions

def elite_8(sweet_results):
    regions = np.empty(4)
    for i in range(4):
        if(winProbability(int(sweet_results[i][0]),int(sweet_results[i][1])) > random.uniform(0,1)):
            regions[i] = sweet_results[i][0]

        else:
            regions[i] = sweet_results[i][1]
                 
    return regions

def final_four(elite_results):
    finals = np.empty(2)
    if(winProbability(int(elite_results[0]),int(elite_results[1])) > random.uniform(0,1)):
        finals[0] = elite_results[0]

    else:
        finals[0] = elite_results[1]

    if(winProbability(int(elite_results[2]),int(elite_results[3])) > random.uniform(0,1)):
        finals[1] = elite_results[2]

    else:
        finals[1] = elite_results[3]

    return finals

def championship(finals_results):
    if(winProbability(int(finals_results[0]),int(finals_results[1])) > random.uniform(0,1)):
        return finals_results[0]
    
    else:
        return finals_results[1]

first = first_round()
second = second_round(first)
sweet = sweet_16(second)
elite = elite_8(sweet)
finals = final_four(elite)
champ = championship(finals)

print(first)
print(second)
print(sweet)
print(elite)
print(finals)
print(champ)