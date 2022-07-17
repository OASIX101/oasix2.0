# d = {'name' : 'anthony',
#     'course' : 'backend',
#     'scores' : [10,7,5,9],
#     'address' : {'str': 2,
#                  'str_name': 'montegory road',
#                  'city' : 'yaba'},
#     ('tuple'): 'this is a tuple'
# }

# # d['name']= 'olowu'
# # print(d['name'])

# # print(max(d['scores']))

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
