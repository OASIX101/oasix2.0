
import random as rd
import time as T
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

y = 'yes'
while continue1 == y:
    play+=1
    print(words)
    print('-----------------------------')
    user_pick = input('Enter your guess: ').lower()
    com_pick = rd.choice(words)    
    if user_pick in words:
        print()
        print('-----------------------------')
        print(f'computer pick: {com_pick}')
        if user_pick == com_pick:
            score+=5
            print('you guessed correctly, 5 points added to total score')
            print(f'you have {limit} trials left')
            print('-----------------------------')
            print()
        else:
            limit-=1
            print('you guessed wrongly')
            print(f'you have {limit} trials left')
            print('-----------------------------')
            print()
    else:
        print('invalid input')      
   
        y = 'yes'
    if limit == 0:
        continue1 = input('if you wish to continue insert "yes" or insert anything to stop: ').lower()
        if continue1 == y:
            limit = 5
            score = 0
            play = 0
            continue
        else:
            print('-----------------------------')
            print(f'Total points accumulated: {score}')
            print(f'Total game won: {score//5}')
            print(f'Total game played: {play}')
            print('-----------------------------')        
            break
