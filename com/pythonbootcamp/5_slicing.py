'''
Created on Nov 8, 2018

@author: Administrator
'''

######### SLICING LISTS!!! #########

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print(numbers[1:])

print(numbers[1:5])

print(numbers[:4])

print(numbers[-3:]) # slice starting from end

print(numbers[:-4]) # how many items excludes

print(numbers[:10:2])

print(numbers[::-1]) # reverses the list

numbers[1:4] = ['a', 'b', 'c']

print(numbers)

######### SWAPPING VALUES #########

names = ["James","Jessie"]

names[0], names[1] = names[1], names[0]

print(names)
