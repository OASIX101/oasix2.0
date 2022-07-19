# for i in range(10):
#     print('attempt')

# a = [1,2,3,4,5,6,7]
# b = []
# for i in a:
#     b.append(i**2)

# print(b)

# # OR #

# b = [i**2 for i in a]
# print(b)

# c = [i for i in a if i%2 == 0]
# print(c)

# d = [i if i%2 == 0 else 0 for i in a]
# print(d)
from math import sqrt

# def number(num):
#     '''this function calculates whether the argument passed
#     is a prime number.

#     returns:
#         true if the number in the is a prime number and
#         false if its not 
#     ''' 

#     if num == 1:
#         return False

#     if num == 2:
#         return True

#     for factor in range(2, int(sqrt(num) + 1)):
#         if num % factor == 0:
#             return False, 'its not a prime number'

#     return True, 'its a prime number'
             
# print(number(37))


# def words(s1:str,s2:str):
#     '''
#        this is a function that checks if to strings are
#        anagrams(contain the same letters) of each other.
    
#     Args:
#         s1(str): this is the first word.
#         s2(str): this is the second word.

#     return:
#         it returns true if they are anagrams of each other
#         and false if the are not.

#     '''
     

#     c = sorted(s1)
#     d = sorted(s2)

#     if c == d:
#         return True
#     else:
#         return False

# print(words('teach','cheate'))



