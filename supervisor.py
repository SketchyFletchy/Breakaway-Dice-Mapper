from breakawayProbability import calculateOutcomes

def runScenario(playerDiceArray, dmDiceArray, diceFace, verbose=False, legacy=False):
    results =  {}
    for playerDiceNo in playerDiceArray:
        player_dice_results = {}
        for dmDiceNo in dmDiceArray:
            player_dice_results[dmDiceNo] = calculateOutcomes(legacy=legacy, verbose=verbose, playerDiceNo=playerDiceNo, dmDiceNo=dmDiceNo, diceFace=diceFace)
        results[playerDiceNo] = player_dice_results
    return results