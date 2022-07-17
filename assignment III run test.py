import random as rd
import time as T
print('WELCOME TO MY GAME !')
T.sleep(0.5)
print('How to play: guess the randomly obtained word correctly and get 5 points')
T.sleep(0.5)
name = input('insert name -> ').upper()
T.sleep(0.5)
print(f'WELCOME MASTER " {name} "')

words  = ('true','boolean','string','integer','superhuman','elephant','casino','checkers','ronaldo')


def game():
    '''this is a guessing game. A word is randomly picked by
        by computer. The user has to correctly guess that word. If
        correct, user gets 5 points.

    Args:
        com_pick(str): randomly picked word by the computer
        user(str): word inputed by the user.

    returns:
        this is the result of the game.

    '''
    print(words)
    com_pick = rd.choice(words)
    user_pick = input('Enter your guess: ').lower()

    if user_pick in words:
        print('------------------------------------')
        print(f'comuputer pick: {com_pick}')
        if user_pick == com_pick:
            print('-----------------------------------') 
            print('you win')
            print('you have 5 added points')
        else:
            print('-----------------------------------')
            print('you lose')
            print('Dont give up!, try again')
    else:
        print('invalid input')      
       


play = 0

while play > -1:
    game()
    play+=1
    continue1 = input('if you wish to continue insert "yes" or insert anything to stop: ').lower()
    y = 'yes'
    if continue1 == y:
        continue
    else:
        print(f'Total game played: {play}')        
        break
