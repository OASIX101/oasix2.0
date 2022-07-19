
import random as rd
import time as T
from urllib.parse import uses_relative
print('WELCOME TO MY GAME !')
T.sleep(0.5)
print('How to play: guess the randomly obtained word correctly and get 5 points')
T.sleep(0.5)
name = input('insert name -> ').upper()
T.sleep(0.5)
print(f'WELCOME MASTER {name}')


words  = ('true','boolean','string','integer','superhuman','elephant','casino','checkers','ronaldo')

score = 0
play = 0
continue1 = input('if you wish to continue insert "yes" or insert anything to stop: ').lower()
limit = 5

while continue1 == 'yes':
    com_pick = rd.choice(words)
    print(words)
    print()
    user_pick = input('enter ur guess: ')
    play+=1
    if user_pick in words:
        print(com_pick)
        print()
        if user_pick == com_pick:
            print('you win, 5 points')
            score+=5
            print(f'you have {limit} trials remaining')
            print()
        else:
            print('you lose,try again')
            limit-=1
            print(f'you have{limit} trials remaining') 
            print()
    else:
        print('invalid input')
        print()

if limit == 0:
    continue1 = input('if you wish to continue insert "yes" or insert anything to stop: ').lower()
    if continue1 != 'yes':
        print(f'total score accumulated: {score}')
        print(f'total game won: {score//2}')
        print(f'total game played: {play}')
    else:
        limit = 5
        score = 0
        play = 0
