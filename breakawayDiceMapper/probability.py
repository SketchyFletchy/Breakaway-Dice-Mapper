from itertools import combinations_with_replacement as cwr
from breakawayDiceMapper.models import models

def lazyGen (noRolls, maxDiceValue) :
    combinations = cwr([x for x in range(1, maxDiceValue+1)][::-1], noRolls)
    return combinations




def calculateOutcomes(playerDiceNo, dmDiceNo, diceFace, model, stat, verbose=False):
    '''
        Takes a number of dice for both player & DM as well as a dice type and returns win percentage
    '''
    wins = 0
    losses = 0
    draws = 0
    rollCounter = 0
    leastRolls = min(playerDiceNo, dmDiceNo)
    playerArray = list(lazyGen(playerDiceNo, diceFace))
    dmArray = list(lazyGen(dmDiceNo, diceFace))

    comparitor = models[model]

    for playerHand in playerArray :
        for dmHand in dmArray :
            rollCounter += 1
            outcome, drawn_dice = comparitor(playerHand, dmHand, leastRolls)
            draws += drawn_dice / leastRolls

            if verbose:
                print (playerHand, "vs", dmHand, ": player", outcome)

            if outcome == 'win':
                wins += 1
            elif outcome == 'lose':
                losses += 1
    if verbose:
        print("Aggregate result:", wins, "successes,", losses, "failures of", rollCounter, "rolls. \nScenario Win:Loss ratio:", wins/losses, "\nProbability of success:", 100*wins/rollCounter, "%")

    if stat == 'win_percentage':
        return wins / rollCounter
    elif stat == 'average_drawn_dice_per_checks':
        return draws / rollCounter
    else:
        print('Unknow stat:', stat)
        quit()