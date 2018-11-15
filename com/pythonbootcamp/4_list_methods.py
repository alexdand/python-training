'''
Created on Nov 8, 2018

@author: Administrator
'''

numbers = [2, 1, 3, 2, 6]

print(f"First index of 2 is : {numbers.index(2)}")

print(f"Second index of 2 is : {numbers.index(2, 1)}")

print(f"Occurences of 2: {numbers.count(2)}")
print(f"Occurences of 999: {numbers.count(999)}")

numbers.reverse()
print(numbers)

numbers.sort()
print(numbers)

words = ["Coding", "is", "fun!"]

print(' '.join(words))
