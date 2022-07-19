# array= [1,2,3,4,5]

# def mean(arr):
#     return sum(arr)/len(arr)

# print(mean(array))

number = 115
limit = 5

while True:
    input1 = input('')
    for input1 in number:
        print(input1)
        if input1== number and limit > 0:
            print('you win')
        elif input1 != number and limit != 0:
            print('try again')
            print(f'you have {limit} lives remaining')
        elif input1!= number and limit == 0:
            print('GAMEOVER !!!')
            limit-=1
        break 



