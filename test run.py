from os import access
import random
# str = '_______'
# index = 0
# new_character = 'F'
# str = str[:index] + new_character + str[index+1:]
# print(str)

# d = {'ant':30}
# f = 20
# if f > d['ant']:
#     d['ant'] = f
# else:
#     print('suiii')

# print(d)
# from random import randint
# p = 'H-' + str(randint(0, 9999)).rjust(4, '0')
# print(p)

# import re 
# s = 'anthony'
# word_size = '_'* len(s)
# substr = "n" 
# result = [_.start() for _ in re.finditer(substr, s)] 
# print(result)

# i = 0
# j = -1
# while i != len(result):
#     j+=1
#     if j in result:
#         run = word_size[:j] + substr + word_size[j+1:]
#         word_size = run
#         i+=1
# print(word_size)
# print("The start indices of the substrings are : " + str(result))
# data2 = {'00020020': {'login_pin' : '12',
#                   'word': 'anthony'}
#                   }
# def login( data: dict):
#     acc_num =  input("Account number:\n>")
#     login_pin = input("Login Code:\n>")
#     user_detail = data.get(acc_num)
    
#     if user_detail and user_detail["login_pin"] == login_pin:
#         return user_detail, acc_num
    
#     else:
#         return None,False

# w,r = login(data2)
# print(w,r)

# # List of weights
# weights = [100, 40, 50]
# # Sort the list
# weights.sort()

# # Unpack
# a, b, c = weights
# # Print Values to Console
# print('Light: ', a)
# print('Medium: ', b)
# print('Heavy: ', c)
data = {}
trans_data = {}
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
    
    return details, trans , var
data, trans_data, acc_num = signup(data, trans_data)

def login(user_detail:dict):
    acc_num =  input("Account number:\n>")
    user_detail = data.get(acc_num)
    if user_detail:
        trans_data[acc_num] = 'you logged in'
    else:
        return 

login(data)        
print(data)
print(trans_data)