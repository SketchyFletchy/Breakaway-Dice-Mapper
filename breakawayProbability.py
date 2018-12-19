from itertools import combinations_with_replacement as cwr

def lazyGen (noRolls, maxDiceValue) :
    combinations = cwr([x for x in range(1, maxDiceValue+1)][::-1], noRolls)
    return combinations

def compareHands (player, dm, rollsPerHand) :
    rollWins = 0
    rollLoses = 0
    for roll in range(rollsPerHand) :
        if player[roll] > dm[roll] :
            rollWins += 1
        elif dm[roll] > player[roll]:
            rollLoses += 1
        else:
            if len(player) > len(dm):
                rollWins += 1
            elif len(dm) > len(player):
                rollLoses += 1
    if rollWins >= rollLoses :
        return 'win'
    else :
        return 'lose'

def legacyCompareHands(player, dm, rollsPerHand):
    rollWins = 0
    rollLoses = 0
    for roll in range(rollsPerHand) :
        if player[roll] >= dm[roll] :
            rollWins += 1
        else:
            rollLoses += 1
    if rollWins >= rollLoses :
        return 'win'
    else :
        return 'lose'

def calculateOutcomes(playerDiceNo, dmDiceNo, diceFace, legacy=False, verbose=False):
    '''
        Takes a number of dice for both player & DM as well as a dice type and returns win percentage
    '''
    wins = 0
    losses = 0
    rollCounter = 0
    leastRolls = min(playerDiceNo, dmDiceNo)
    playerArray = list(lazyGen(playerDiceNo, diceFace))
    dmArray = list(lazyGen(dmDiceNo, diceFace))

    comparitor = legacyCompareHands if legacy else compareHands

    for playerHand in playerArray :
        for dmHand in dmArray :
            rollCounter += 1
            outcome = comparitor(playerHand, dmHand, leastRolls)

            if verbose:
                print (playerHand, "vs", dmHand, ": player", outcome)

            if outcome == 'win':
                wins += 1
            elif outcome == 'lose':
                losses += 1
    if verbose:
        print("Aggregate result:", wins, "successes,", losses, "failures of", rollCounter, "rolls. \nScenario Win:Loss ratio:", wins/losses, "\nProbability of success:", 100*wins/rollCounter, "%")

    return wins / rollCounter