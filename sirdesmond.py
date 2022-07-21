import random



def guess_game(trial:int, score:int):
    """This function allows users to guess what the computer has selected.
    
    
    Args:
        trial (int): This is the total number of trials selected
        score (int): This is the score of the user at the time of function call.
        
    Returns:
        trial (int): This is the total trials left after the function call
        score (int): This is the total score left after the function call."""  
    
    
    num = list(range(53, 60))
    random.shuffle(num)

    print("You can select from the list below.")
    print(num)
    com_choice = random.choice(num)
    user_choice = int(input(">"))

    if user_choice in num:
        if user_choice == com_choice:
            print("You win!")
            print("You just got an extra trial!")
            score+=3
        else:
            trial -=1
            if user_choice > com_choice:
                print("Too High")
            else:
                print("Too low")
                
        print(f"Computer choice: {com_choice}")
    else:
        trial -=1 
        print("Invalid input")
    return score, trial 


def login(data:dict, score:int):
    
    """This function takes a dictionary, asks the user for the name and adds their name to the dictionary.
    
    Args:
        data(dict) : This is the dictionary that stores the user data
    
    Returns:
        name (str): This is the name of the user
    """
    
    name = input("Name: ").lower()

    data[name] = score
    return name

trials = 3
score = 0
with open("database.txt", "r") as file:
    data = eval(file.read())
    # print(type(data))
    
    
# print(eval("3") + eval("3"))

name = login(data, score)

while trials > 0:
    

    score, trials = guess_game(trials, score)
    
    if trials == 0:
        
        if score > data[name]:
            print(f"Your new high score is {score}")
            data[name] = score
        else:
            print(f"You scored {score} points.")
        
        
        print("Do you want to play again? Y/n?")
        rematch = input("> ").lower() 
        
        if rematch == "y":
            "Print welcome back"
            trials = 3
            score = 0

            name = login(data, score)
        else:
            print("Game over!")


with open("database.txt", "w") as file:
    file.write(str(data))
