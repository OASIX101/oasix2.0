import random

with open("bankcorrect.txt") as file:
    data = eval(file.read())
with open("bank correct2.txt") as file:
    trans_data = eval(file.read())
    

def signup(details : dict, trans:dict):
    """ This function takes in a dictionary, asks the user for input details then generates a random account number for the user. It then adds the user data to the original dictionary and returns the updated dictionary. """
    
    
    first_name = input("First Name:\n>")
    last_name = input("Last Name:\n>")
    trans_pin = input("Transaction Pin:\n>")
    login_pin = input("Login Code:\n>")


    var = "0"
    for i in range(9):
        var += str(random.choice(range(10)))
    
    

    details[var] = {"first_name":first_name,
                    "last_name" : last_name,
                    "login_pin" : login_pin,
                    "transaction_pin": trans_pin,
                    "balance" : 0}
    trans[var] = []
    
    print(f"You have successfully created an account. Your account number is {var}. You can login to your account using your login code: {login_pin}")
    
    return details, trans


def login( data: dict):
    acc_num =  input("Account number:\n>")
    login_pin = input("Login Code:\n>")
    user_detail = data.get(acc_num)
    
    if user_detail and user_detail["login_pin"] == login_pin:
        return user_detail, acc_num
    
    else:
        return False, 'incorrect pin'
    
        
def deposit(user_detail:dict):
    
    amount = float(input("How much to deposit\n>"))
    user_detail["balance"] += amount
    print(f"\nYour wallet has been credited with #{amount}")
    return user_detail, amount


def withdraw(user_detail:dict):
    
    trans_pin = input("Enter your pin\n>")
    
    if trans_pin == user_detail["transaction_pin"]:
        amount = float(input("How much to withdraw\n>"))
        
        if user_detail["balance"] > amount:
            user_detail["balance"] -= amount
            print(f"\nWithdraw of #{amount} was successful")
            return user_detail, amount
        else:
            print("\nInsufficient funds to withdraw")
        
    else:
        print("\nIncorrect pin")
        return
     
def transfer(user_detail:dict, data:dict):
    beneficiary = input("Enter beneficiary account\n>")
    amount = float(input("How much to transfer\n>"))
    
    beneficiary_detail = data.get(beneficiary)
    if beneficiary_detail:
        if user_detail["balance"] > amount:
            user_detail["balance"] -= amount
            beneficiary_detail["balance"] += amount
            print(f"Transfer of #{amount} was successful")
            return user_detail, data,amount, beneficiary
        
        else:
            amount=None
            print("\nInsufficient funds to transfer")
            return user_detail, data,amount, beneficiary
    else:
        amount=None
        print("\nUnable to transfer to unknown account.")
        return user_detail, data, amount, beneficiary
        
        
def update_transaction(trans_data:dict, acc_num:str, trans_type:str, action:str, amount:float):
    trans_detail = {
        "amount":amount,
        "action":action,
        "trans_type":trans_type,
    }
    trans_data[acc_num].append(trans_detail)
    return trans_data
        
        
        
print("Welcome to ClassikAlat")

while True:
    print("\nEnter L to login or S to signup or Q to quit.")
    choice = input(">").lower()
    if choice == "s":
        data, trans_data = signup(data, trans_data)

    elif choice == "l":
        user_detail, acc_num = login(data)
        
        if user_detail:
            print("\nWelcome", user_detail["first_name"])
            while True:
                print("""Enter the corresponding number for the action you wish to perform.
                1. Check Balance
                2. Deposit
                3. Withdraw
                4. Transfer
                5. Recent Transactions
                6. Logout
                    """)
                action  = input(">")
                if action == "1":
                    print(f"\nYour account balance is #{user_detail['balance']}")
                elif action == "2":
                    user_detail, amount = deposit(user_detail)
                    trans_data = update_transaction(trans_data, acc_num, "credit","deposit", amount)
                    
                elif action == "3":
                    user_detail, amount = withdraw(user_detail)
                    trans_data = update_transaction(trans_data, acc_num, "debit","withdraw", amount)
                elif action == "4":
                    user_detail, data,amount,beneficiary  = transfer(user_detail, data)
                    
                    if amount is not None:
                        trans_data = update_transaction(trans_data, acc_num, "debit","transfer", amount)
                        trans_data = update_transaction(trans_data, beneficiary, "credit","transfer", amount)
                elif action == "5":
                    arr = trans_data.get(acc_num)
                    arr.reverse()
                    if len(arr) >= 5:
                        for i in range(5):
                            transaction = arr[i]
                            print("===================")
                            print(f"Amount: #{transaction['amount']}") 
                            print(f"Action: {transaction['action']}")
                            print(f"Transaction type:{transaction['trans_type']}")
                        print("===================\n")
                    else:
                        for i in range(len(arr)):
                            transaction = arr[i]
                            print("===================")
                            print(f"Amount: #{transaction['amount']}") 
                            print(f"Action: {transaction['action']}")
                            print(f"Transaction type: {transaction['trans_type']}")
                        print("===================\n")
                elif action == "6":
                    print("\nLog out complete!")
                    break
                else:
                    print("\nInvalid input")
        else:
            print("Invalid account number or pin")

    elif choice == "q":
        print("\nBye!")
        break
    else:
        print("\nInvalid input")
        
with open("bankcorrect.txt", "w") as file:
    file.write(str(data))
with open("bank correct2.txt", "w") as file:
    file.write(str(trans_data))
    



s = "Anthony"
import re 
 
 
#defining substring 
substr = "n"
 
 
 
result = [_.start() for _ in re.finditer(substr, s)] 
 
print("The start indices of the substrings are : " + str(result))