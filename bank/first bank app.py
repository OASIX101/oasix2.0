from random import randint
print('welcome to oasix bank')
data = {}


num = "0" + str(randint(0,999999999)).rjust(9, '0')
with open('bank database.txt','r') as file:
    data = eval(file.read())

while True:
    request = input('Do you have an account here?. Enter "yes" if you have or "no" if you dont\n>>> ').lower()
    if request == 'yes':
        acct_num = str(input('Enter your account number\n>>>'))
        if acct_num in data.keys():
            print('welcome', data[acct_num]['first_name'], data[acct_num]['last_name'])
            login_pin = input('Enter your login pin.\n>>>')
            if login_pin == data[acct_num]['login_pin']:
                option = int(input('What would you like to do? insert 1,2,3,4,5,6 ->\n1. check account balance\n2. Transfers\n3. Deposit\n4. Withdraw\n5. change login pin\n6. change transaction pin\n>> '))
                options =  [1,2,3,4,5,6]
                

                if option in options:
                    pin = data[acct_num]['transaction_pin']
                    if option == 1:
                        en = input('Enter transaction pin\n>>>')
                        if en == pin:
                            print('your balance is $',data[acct_num]['balance'])
                        else:
                            print('incorrect pin')

                    elif option == 2:
                        person = input('Enter the user account number.\n>>>')
                        if person in data:
                            amount = int(input('Enter amount.\n$'))
                            en = input('Enter transaction pin\n>>>')
                            if en == pin:
                                data[person]['balance']+=amount
                                data[acct_num]['balance']-=amount
                                print(f'${amount} has be transferred to {person}', data[person]['first_name'], data[person]['last_name'])
                            else:
                                print('incorrect pin')
                        else:
                            print('user invalid')
                    
                    elif option == 3:
                        en = input('Enter transaction pin\n>>>')
                        if en == pin:
                            dep = int(input('Enter amount\n>>>'))
                            data[acct_num]['balance']+=dep
                            print(f'Your new balance is ${data[acct_num]["balance"]}')
                        else:
                            print('incorrect pin')

                    elif option == 4:
                        en = input('Enter transaction pin\n>>>')
                        if en == pin:
                            withdrawal = int(input('Enter amount\n>>>'))
                            draw = data[acct_num]['balance']
                            if withdrawal > draw:
                                print(f'insufficient balance\n balance is {draw}')
                            else:
                                data[acct_num]['balance']-=withdrawal
                                print(f'Your new balance is $', data[acct_num]['balance'])
                        else:
                            print('incorrect pin')

                    elif option == 5:
                        login_pin1 = data[acct_num]['login_pin']
                        en1 = input('Enter previous login pin\n>>>')
                        while True:
                            if en1 == login_pin1:
                                change = input('Enter new pin\n>>>')
                                if len(change) == 4:
                                    change1 = input('Enter new pin again for clearity\n>>>')
                                    if change1 == change:
                                        data[acct_num]['login_pin'] = change1
                                        print(f'pin successfully changed to {change1}\nDo not forget it')
                                        break
                                    else:
                                        print('inputed pin do not match')
                                else:
                                    print('inputed pin is not up to 4 digits')
                            else:
                                print('invalid pin')
                                break

                    elif option == 6:
                        trans_pin2 = data[acct_num]['transaction_pin']
                        en2 = input('Enter previous transaction pin\n>>>')
                        while True:
                            if en2 == trans_pin2:
                                change3 = input('Enter new pin\n>>>')
                                if len(change3) == 4:
                                    change4 = input('Enter new pin again for clearity\n>>>')
                                    if change3 == change4:
                                        data[acct_num]['transaction_pin'] = change4 
                                        print(f'pin successfully changed to {change4}\nDo not forget it')
                                        break
                                    else:
                                         print('inputed pin do not match')
                                else:
                                    print('inputed pin is not up to 4 digits')
                            else:
                                print('invalid pin')
                                break

                else:
                    print('invalid input')

                with open('bank database.txt','w') as file:
                    file.write(str(data))
            else:
                print('incorrect pin')   
            
        else:
            print('USER NOT FOUND')        
    
    elif request == 'no':
        acct = num
        if acct not in data:
            print(f'Your account is {acct}, keep for future reference')
            data.update({f'{acct}':{"first_name":"",
                                "last_name" : "",
                                "login_pin" : "",
                                "transaction_pin": "",
                                "balance" : 5000}
                                })

            info = input('Enter your first name(surname)\n>>>')
            data[acct]['first_name'] = info
            info2 = input('Enter your last name\n>>>')
            data[acct]['last_name'] = info2
            while True:
                info1 = input('Set transaction pin. 4 digits not to be shown to anyone\n>>>')
                if len(info1) == 4:
                    data[acct]['transaction_pin'] = info1
                    break
                elif len(info1) > 4:
                    print('inserted pin greated than 4')
                elif len(info1) < 4:
                    print('inserted pin less than 4')
            while True:
                info3 = input('Set login pin. 4 digits not to be shown to anyone\n>>>')
                if len(info3) == 4:
                    data[acct]['login_pin'] = info3
                    break
                elif len(info3) > 4:
                    print('inserted pin greated than 4 digits')
                elif len(info3) < 4:
                    print('inserted pin less than 4 digits')

            print(f'Account sucessfully created.\nWelcome to oasix bank {info} {info2}\nyour number is {acct} ')
            with open('bank database.txt', 'w') as file:
                file.write(str(data))
        
    else:
        print('invalid input')
    

    restart = input('Do you wish to continue.\nInsert "c" to continue or "s" to stop\n>>>').lower()
    if restart == 'c':
        continue
    elif restart == 's':
        print('Have a great day our dear customer!!!')
        break
    else:
        print('Have a great day beloved customer!!!')
        break



