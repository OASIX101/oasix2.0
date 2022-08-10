from random import randint

with open('bank copy.txt', 'r') as file:
    data = eval(file.read())


def create_acct():
    fname = input('Enter your first name(surname)\n>>>').capitalize()
    data[num1]['first_name'] = fname
    lname = input('Enter your last name\n>>>').lower()
    data[num1]['last_name'] = lname
    print(f'welcome {fname} {lname} ')
    while True:
        info3 = input('Set login pin. 4 digits not to be shown to anyone\n>>>')
        if len(info3) == 4:
            data[num1]['login_pin'] = info3
            break
        elif len(info3) > 4:
            print('inserted pin greated than 4 digits')
        elif len(info3) < 4:
            print('inserted pin less than 4 digits')

    while True:
        info1 = input('Set transaction pin. 4 digits not to be shown to anyone\n>>>')
        if len(info1) == 4:
            data[num1]['transaction_pin'] = info1
            break
        elif len(info1) > 4:
            print('inserted pin greated than 4')
        elif len(info1) < 4:
            print('inserted pin less than 4')

    print(f'Your account number is {num1}\nkeep for future reference')
    print(f'Thank you for choosing oasix bank {fname} {lname}')

def transaction():
    choice = int(input('what would you like to do\n1. check account balance\n2. make a deposit\n3. transfer\n4. withdraw\n5. change login pin\n6. change transaction pin\n>>>'))
    choices = [1,2,3,4,5,6]
    if choice in choices:
        if choice == 1:
            balance_check()

        elif choice == 2:
            deposit()

        elif choice == 3:
            transfer()

        elif choice == 4:
            withdraw()

        elif choice == 5:
            pinchange_login()

        elif choice == 6:
            pinchange_trans()     
        else:
            print('invalid input')
    else:
        print('input option not in the options')

def balance_check():
    en = input('Enter transaction pin\n>>>')
    pin = data[num2]['transaction_pin']
    if en == pin:
        print('your balance is $',data[num2]['balance'])
    else:
        print('incorrect pin')

def transfer():
    pin = data[num2]['transaction_pin']
    person = input('Enter the user account number.\n>>>')
    if person in data:
        amount = int(input('Enter amount.\n$'))
        en = input('Enter transaction pin\n>>>')
        if en == pin:
            data[person]['balance']+=amount
            data[num2]['balance']-=amount
            print(f'${amount} has be transferred to {person}', data[person]['first_name'], data[person]['last_name'])
        else:
            print('incorrect pin')
    else:
        print('user not found')

def deposit():
    pin = data[num2]['transaction_pin']
    en = input('Enter transaction pin\n>>>')
    if en == pin:
        dep = int(input('Enter amount\n>>>'))
        data[num2]['balance']+=dep
        print(f'Your new balance is ${data[num2]["balance"]}')
    else:
        print('incorrect pin')

def withdraw():
    pin = data[num2]['transaction_pin']
    en = input('Enter transaction pin\n>>>')
    if en == pin:
        withdrawal = int(input('Enter amount\n>>>'))
        draw = data[num2]['balance']
        if withdrawal > draw:
            print(f'insufficient balance\n balance is {draw}')
        else:
            data[num2]['balance']-=withdrawal
            print(f'Your new balance is $', data[num2]['balance'])
    else:
        print('incorrect pin')

def pinchange_login():
    login_pin1 = data[num2]['login_pin']
    en1 = input('Enter previous login pin\n>>>')
    while True:
        if en1 == login_pin1:
            change = input('Enter new pin\n>>>')
            if len(change) == 4:
                change1 = input('Enter new pin again for clearity\n>>>')
                if change1 == change:
                    data[num2]['login_pin'] = change1
                    print(f'pin successfully changed to {change1}\nDo not forget it')
                    break
                else:
                    print('inputed pin do not match')
            else:
                print('inputed pin is not up to 4 digits')
        else:
            print('invalid pin')
            break
    
def pinchange_trans():
    trans_pin2 = data[num2]['transaction_pin']
    en2 = input('Enter previous transaction pin\n>>>')
    while True:
        if en2 == trans_pin2:
            change3 = input('Enter new pin\n>>>')
            if len(change3) == 4:
                change4 = input('Enter new pin again for clearity\n>>>')
                if change3 == change4:
                    data[num2]['transaction_pin'] = change4 
                    print(f'pin successfully changed to {change4}\nDo not forget it')
                    break
                else:
                        print('inputed pin do not match')
            else:
                print('inputed pin is not up to 4 digits')
        else:
            print('invalid pin')
            break 

def verify_acct():
    acct_verify = input('Enter your acct number\n>>>')
    if acct_verify in data.keys():
        print('This account exists\n')
    else:
        print('Account not found\nGo to the main menu to create an account\n')


while True:
    option = int(input('what would like to do\n1. create an account\n2. Log in to an existing account\n3. verify whether your account exists\n>>>'))
    options = [1,2,3]
    num = '0' + str(randint(0, 999999999)).rjust(9, '0')

    if option in options:
        num1 = num
        if option == 1:
            if num1 not in data.keys():
                data.update({f'{num1}':{"first_name":"",
                                            "last_name" : "",
                                            "login_pin" : "",
                                            "transaction_pin": "",
                                            "balance" : 5000}
                                            })

                create_acct()
                with open('bank copy.txt','w') as file:
                    file.write(str(data))
    
        elif option == 2:
            num2 = input('Enter your account number\n>>> ')
            if num2 in data.keys():
                log_verify = input('Enter your login pin\n>>> ')
                if log_verify == data[num2]['login_pin']:
                    print('welcome back', data[num2]['first_name'], data[num2]['last_name'])
                    transaction()
                else:
                    print('login pin not correct')
            else:
                print('USER NOT FOUND')
            
            with open('bank copy.txt', 'w') as file:
                file.write(str(data))

        elif option == 3:
            verify_acct()

    else:
        print('invalid input')
    
    restart = input('what do you wish to do\n1. Main menu\n2. Log out\n>>> ')
    print('')

    if restart == '1':
        continue
    elif restart == '2':
        print('Have a great day\nWe hope to see you again')
        break
    else:
        print('Have a great day\nWe hope to see you again')
        break

    
                