import random
'''
Additonal models can be defined here.

Models must take inputs (player, dm, rollsPerHand)
    where player is the player hand array
    dm is the dm hand array
    and rollsPerhand is how many rolls can be compared

Models must output either:
    "win", drawn_dice
        or
    "lose", drawn_dice

    where "win" means player succeeds overall
    where "lose" means player fails overall
    where drawn_dice is the count of individual dice pairs which resulted in a draw
'''

def legacy(player, dm, rollsPerHand):
    '''
    Original model by Fez.
    Individual dice ties go to player.
    '''
    rollWins = 0
    rollLoses = 0
    drawn_dice = 0

    for roll in range(rollsPerHand) :
        if player[roll] >= dm[roll] :
            rollWins += 1
        else:
            rollLoses += 1
    if rollWins >= rollLoses :
        return 'win', drawn_dice
    else :
        return 'lose', drawn_dice

def throwOutDraws (player, dm, rollsPerHand) :
    '''
    Propsed model 1 by Griff & Fletch
    Individual dice ties are discarded.
    Tied number of successes goes side with most dice
    '''
    rollWins = 0
    rollLoses = 0
    drawn_dice = 0

    for roll in range(rollsPerHand) :
        if player[roll] > dm[roll] :
            rollWins += 1
        elif dm[roll] > player[roll]:
            rollLoses += 1
        else:
            # Ignore drawn dice
            drawn_dice += 1
    if rollWins >= rollLoses :
        return 'win', drawn_dice
    else :
        return 'lose', drawn_dice

def skillBiasedDraws (player, dm, rollsPerHand) :
    '''
    Propsed model 2 by Griff & Fletch
    Individual dice ties go to side with most dice.
    If sides have equal dice, draws are ignored.
    Tied number of successes goes side with most dice
    '''
    rollWins = 0
    rollLoses = 0
    drawn_dice = 0

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
            else:
                drawn_dice += 1
    if rollWins >= rollLoses :
        return 'win', drawn_dice
    else :
        return 'lose', drawn_dice

def randomlySettledDraws(player, dm, rollsPerHand) :
    '''
    Altrnative to models 1&2 propozed by Fez
    Individual dice ties are ignored.
    Tied number of successes goes player on a 1d6 roll > 3
    '''
    rollWins = 0
    rollLoses = 0
    drawn_dice = 0

    for roll in range(rollsPerHand) :
        if player[roll] > dm[roll] :
            rollWins += 1
        elif dm[roll] > player[roll]:
            rollLoses += 1
        else:
            drawn_dice += 1
    if rollWins > rollLoses :
        return 'win', drawn_dice
    elif rollWins < rollLoses:
        return 'lose', drawn_dice
    else:
        if random.random() >= 0.5:
            return 'win', drawn_dice
        else:
            return 'loss', drawn_dice

# exported models lookup table
models = {
    'legacy':legacy,
    'throwOutDraws':throwOutDraws,
    'skillBiasedDraws':skillBiasedDraws,
    'randomlySettledDraws':randomlySettledDraws
}