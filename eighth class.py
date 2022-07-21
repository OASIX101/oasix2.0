# with open('C:/Users/CC/Desktop/oasix.py.txt', 'w')  as r:
#     r.write('i just wrote to my desktop')
#     r.write('\n\ti just appended ')    

def mean(*numbers):
    for i in numbers:
        return sum(numbers) / len(numbers)

mean1 = mean(1,7,6,2,3,4,5)

def median(list_of_numbers):
    list_of_numbers.sort()
    if len(list_of_numbers) % 2 == 1:
        middle_num = int((len(list_of_numbers) -1) / 2)
        return list_of_numbers[middle_num] 
    elif len(list_of_numbers) % 2 == 0:
        middle_num1 = int(len(list_of_numbers) / 2)
        middle_num2 = int(len(list_of_numbers) / 2) -1
        mean_of_median = mean([list_of_numbers[middle_num1],list_of_numbers[middle_num2]])
        return mean_of_median

median1 = median([1,7,6,2,3,4,5])


def variance(list_of_numbers):
    num = len(list_of_numbers)
    mean = sum(list_of_numbers) / num
    dev = [(x - mean) ** 2 for x in list_of_numbers]
    variance = (sum(dev) / num)
    return variance

variance1 = variance([1,7,6,2,3,4,5])

def S_D():
    standard = variance1**0.5
    return standard

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


with open('oasix.py.txt', 'w') as mean2:
    mean2.write(f'the mean is {mean1}\nthe median is {median1}\nthe variance is {variance1}\nthe standard deviation of the numbers is {S_D()}')
    mean2.write(f'\nthe mode is {mode[0]}\nresults added')