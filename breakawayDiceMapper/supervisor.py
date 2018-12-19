from breakawayDiceMapper.probability import calculateOutcomes

def runScenario(player_dice, dm_dice, face, stat, model, verbose=False):
    results =  {}
    for playerDiceNo in player_dice:
        player_dice_results = {}
        for dmDiceNo in dm_dice:
            player_dice_results[dmDiceNo] = calculateOutcomes(model=model, verbose=verbose, playerDiceNo=playerDiceNo, dmDiceNo=dmDiceNo, diceFace=face, stat=stat)
        results[playerDiceNo] = player_dice_results
    return results