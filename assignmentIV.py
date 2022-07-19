numbers = [10, 11, 11, 13, 12, 140, 15, 15, 12, 13, 13, 15, 15, 15, 15, 140, 140, 140, 140]
nums = {}

for i in numbers:
    if i not in nums:
        nums[i] = 1
    else:
        nums[i]+= 1

new_numbers = []
for key, value in nums.items():
    new_numbers.append((value,key))
rearranged_numbers = sorted(new_numbers, reverse=True)

mode = []
for tony,anthony in rearranged_numbers:
    mode.append((anthony))

print(f'the most frequent value is: {mode[0]}')
print(f'the second most frequent number is: {mode[1]}')
print(f'the third most frequent number is {mode[2]}')

#####   EXPLANATION    #####
# line 2:is an empty set
# line 4 - 8: it is used to count the numbers in the list and
            # add the count nums to the empty set to creat a dictionary
# line 10-13: i created a list to add the counted numbers and add them to the didctionary to
            # to create key-value pairs and then reversed it for max to min
# line 15-17: i appended the keys of the number so i can print the number later on
            # and used the index to get the appended value with is the highest value
# line 19-22: i used string formatting to print the words and printed the appended value.

# i think there are other ways to do it using lambda, mapping and other functions which
#  which could make the code simple and understandable. 
