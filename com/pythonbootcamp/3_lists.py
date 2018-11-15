'''
Created on Nov 8, 2018

@author: Administrator
'''

# append, insert, extend

numbers = [1, 2, 3, 4, 6]

numbers.insert(4, 5)
print(numbers)

numbers.append(7)
print(numbers)

numbers.extend([8, 9, 10])
print(numbers)

# clear, pop, remove

last_number = numbers.pop()
print(f"Last number: {last_number}")
print(numbers)

middle_number = numbers.pop(int(len(numbers)/2))
print(f"Middle number: {middle_number}")
print(numbers)

removed_number = numbers.remove(1)
print(removed_number) # gives None
print(numbers)

removed_number = numbers.remove(999) # generates an error 999 not in list