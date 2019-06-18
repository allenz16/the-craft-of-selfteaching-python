from random import randrange

coinUser, coinBot = 10, 10
roundOfGames = 0


def bet(dice, wager):
    if dice == 7:
        print(f'the dice is {dice};\ndraw!\n')
        return 0
    elif dice < 7:
        if wager == 's':
            print(f'the dice is {dice};\nyou win!\n')
            return 1
        else:
            print(f'the dice is {dice};\nyou lose!\n')
            return -1
    elif dice > 7:
        if wager == 's':
            print(f'the dice is {dice};\nyou lose!\n')
            return -1
        else:
            print(f'the dice is {dice};\nyou win!\n')
            return 1


while True:
    print(f'you: {coinUser}\t bot: {coinBot}')
    dice = randrange(2, 13)
    wager = input("what's your bet? : ")
    if wager == 'q':
        break
    elif wager in 'bs':
        result = bet(dice, wager)
        coinUser += result
        coinBot -= result
        roundOfGames += 1
    if coinUser == 0:
        print("gg, you've lost the game.")
        break
    if coinBot == 0:
        print("gg, you've won against bot")
        break

print(f"you've played {roundOfGames} rounds.\n")
print(f"you have {coinUser} coins now.\nbye!")


