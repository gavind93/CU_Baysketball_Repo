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