# numbers = 1
# while True:
#     print(numbers, end= f'+1 = {numbers + 1} ,')
#     numbers+=1
#     if numbers == 11:
#         break

# i = 1
# while i < 10 or i == 10: # i <=10
#     print(i)
#     i+=1


# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j, end = '-')

#     print('') 

# for i in range(1,6):
#     for j in range(1, i + 1):
#         print(j, end= ' ')

#     print(' ')


# s = 0 
# num = int(input('enter number -> '))
# for i in range(num+1):
#     s+=i

# print(f'sum is: {s}')

# n= int(input('- '))
# x = range(n+1)
# s = sum(x)

# print(s)


# n = int(input('number = '))

# for i in range(1,11):
#     i*=n
#     print(i)

# numbers = [12,75,150,180,145,525,50]

# for i in numbers:
#     if i > 500:
#         break
#     elif i > 150:
#        continue
#     elif i % 5 == 0:
#         print(i)

n = 75869
c=0
while n!= 0:
    n = n // 10
    c= c + 1
print(c)