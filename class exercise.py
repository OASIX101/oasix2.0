# class Person:

#     def __init__(self,n1 ,n2):
#         self.n1 = n1
#         self.n2 = n2

#     def talk(self):
#         return f'{self.n1} speaks {self.n2}'


# person1 = Person('anthony', 'english')
# person2 = Person('ore' ,'yoruba')
# person3 = Person('enoch', 'spanish')

# print(person3.talk())


# class  Person2:
#     def __init__(self, name):
#         self.name = name

#     def talk(self):
#         return f'Hi, I am {self.name}'

# person4 = Person2('joshua steffledon')
# print(person4.talk())


# class  Person_inherit(Person):
#     def __init__(self, n1, n2):
#         self.n1 = n1
#         self.n2 = n2

# person4 = Person_inherit('joshua steffledon', 'french')
# print(person4.talk())

# d = {'name' : 'anthony',
#     'course' : 'backend',
#     'scores' : [10,7,5,9],
#     'address' : {'str': 2,
#                  'str_name': 'montegory road',
#                  'city' : 'yaba'},
#     ('tuple'): 'this is a tuple'
# }

# d.update({'tony':{'you':'3',
#                    'no': 'no'}})
# print(d['tony']['you'])
# d['name']= 'olowu'
# print(d['name'])

# print(max(d['scores']))

# # print(sum(d['scores'])/len(d['scores']))

# # print(d['address']['str_name'])

# # print(type(d['address']['city']))

# # print(d[('tuple')])

# # print(d.get('boy'))#prints none if key not found  
# # print(d.get('boy','not found'))#prints not found if key is not found
# # print(d.get('name'))#bringsout the value of the key

# # print(d.keys())
# # print(d.items())
# # print(d.values())

# # print(d.pop('name'))
# # print(d)

# # d['new'] = 'Play'
# # print(d)

# # d['new_name'] = d.pop('name')
# # print(d)  

# data = {'5' : 8,
#         '3' : 10,
#         '4' : 2,
#         '9' : 3,
#         '2' : 7,
#         '0' : 5}

# sorted_x = sorted(data.items(),
# key= lambda x: x[1], reverse=True)

# print(dict(sorted_x))



# map_dict = {'name': 'anthony',
#             'd': 'dance'
# }

# list1 = ['1','3','6','7','9']
# list2 = [1,4,6,7,8]

# zipped = dict(zip(list1,list2))
# map_dict['list'] = zipped
# print(map_dict)



# list= {'v1': 's001',
#        'v2': 's002',
#        'v3': 's004',
#        'v4': 's005',
# }

# value = list.values()
# print(set(value))

#####   loops   #####


# while True:
#     data = int(input('-> '))
#     print(data)
#     if data == 5:
#         break

# a = 100
# count = 0
# while True:
#     print(a)
#     a-=1
#     count+=1
#     if count == 3:
#         break
# from random import randint

# def generate_pin():
#     numee = print(str(randint(0,9999)).rjust(4,"0"))
#     return numee