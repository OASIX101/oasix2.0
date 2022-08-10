import time
import random
import re
with open('gamedatabase.txt', 'r') as file:
    data = eval(file.read())

print('WELCOME TO MY GUESSING GAME')
time.sleep(0.5)
print('How to play: A word would be selected at random\nyou are to guess the letters of that word under a number of trials')
time.sleep(0.5)
print()
name = input('Enter your name: ').capitalize()
print('Welcome master', name,'\n')
words = ['flcock', 'producce', 'pynattive', 'rrandom', 'rodund', 'codindg']
com_pick = random.choice(words)
word_size = '_' * len(com_pick)

trial = 5 
score = 0

alphabet = 'abcdefghijklmnopqrstuvwxyz'

while trial > 0:
    print(alphabet.upper())
    print(f'Guess the letters \n{word_size}')
    user_pick = input('Enter your guess\n- ').lower()
    if user_pick != '':
        if user_pick in com_pick:
            new = alphabet.replace(user_pick, '')
            alphabet = new
            index = [_.start() for _ in re.finditer(user_pick, com_pick)] 
            new_character = user_pick
            i = 0
            j = -1
            while i != len(index):
                j+=1
                if j in index:
                    i+=1
                    run = word_size[:j] + new_character + word_size[j+1:]
                    word_size = run
            score+=5
            print(word_size)
            print(f'you have {trial} trial(s) left\n')

            if word_size == com_pick:
                alphabet = 'abcdefghijklmnopqrstuvwxyz'
                print('YOU WIN !!')
                print('you have', score, 'points' f'\nguess the new word\nyou have {trial} trial(s) left\n')                
                com_pick = random.choice(words)
                word_size = '_' * len(com_pick)
        else:
            trial -=1
            print(f'you have {trial} trial(s) left')
            if trial == 0:
                print('gameover!!!\nThe word was', com_pick)
                print(f'you scored a total of {score} points\n')
                if name not in data.keys():
                    data[name] = score
                    with open('gamedatabase.txt', 'w') as file:
                        file.write(str(data))

                if score > data[name]:
                    print('you have a new highscore', name,'\n')
                    data[name] = score
                    with open('gamedatabase.txt', 'w') as file:
                        file.write(str(data))
                            
    elif user_pick == '':
        print('invalid input\n')
        
    else:
        print('invalid input\nenter a correct alphabet\n')
        
print('\n========= Leaderboard ========')
sorted_x = sorted(data.items(),
key= lambda x: x[1], reverse=True)

for i in dict(sorted_x):
    print('-> ',f'{i}- {data[i]}')


