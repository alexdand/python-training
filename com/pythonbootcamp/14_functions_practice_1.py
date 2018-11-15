'''
Created on Nov 12, 2018

@author: Administrator
'''

##################### EXCERCISE 1 #####################
# Write a function called multiple_letter_count.
# This function takes in one parameter (a string) and returns a dictionary with the keys being the letters and the values being the count of the letter.

def multiple_letter_count(stringy):
    return { letter:stringy.count(letter) for letter in stringy }

print(multiple_letter_count('awesome'))

##################### EXCERCISE 2 #####################
# Write a function called list_manipulation. This function should take in four parameters (a list, command, location and value).
# If the command is "remove" and the location is "end", the function should remove the last value in the list and return the value removed
# If the command is "remove" and the location is "beginning", the function should remove the first value in the list and return the value removed
# If the command is "add" and the location is "beginning", the function should add the value (fourth parameter) to the beginning of the list and return the list
# If the command is "add" and the location is "end", the function should add the value (fourth parameter) to the end of the list and return the list

def list_manipulation(lista, command, location, value = None):
    if command == "remove":
        if location == "end":
            return lista.pop()
        elif location == "beginning":
            return lista.pop(0)
    elif command == "add":
        if location == "beginning":
            lista.insert(0, value)
        elif location == "end":
            lista.append(value)
    return lista


##################### EXCERCISE 3 #####################
# Write a function called is_palindrome. This function should take in one parameter and returns True or False depending on whether it is a palindrome.

def is_palindrome(s):
    return all(s[i]==s[-i-1] for i in range(0, int(len(s)/2)))
# return string == string[::-1]

##################### EXCERCISE 4 #####################
# Write a function called frequency.
# This function accepts a list and a search_term (this will always be a primitive value) and returns the number of times the search_term appears in the list.

def frequency(lista, item):
    return lista.count(item)

##################### EXCERCISE 5 #####################
# Write a function called multiply_even_numbers. This function accepts a list of numbers and returns the product of all even numbers in the list.

def multiply_even_numbers(lista):
    total = 1
    for n in lista:
        if n % 2 == 0:
            total *= n
    return total

##################### EXCERCISE 6 #####################
# Write a function called capitalize. This function accepts a string and returns the same string with the first letter capitalized.
# You may want to use slices to help you out.

def capitalize(string):
    return string[:1].upper() + string[1:]

##################### EXCERCISE 7 #####################
# Write a function called compact. This function accepts a list and returns a list of values that are truthy values, without any of the falsey values.

def compact(lista):
    return [v for v in lista if v]

##################### EXCERCISE 8 #####################
# Write a function called intersection. This function should accept two lists and return a list with the values that are in both input lists.

def intersection(list1, list2):
    return [ val for val in set(list1) & set(list2) ]

##################### EXCERCISE 9 #####################
# Write a function called partition. This function accepts a list and a callback function (which you can assume returns True or False). 
# The function should iterate over each element in the list and invoke the callback function at each iteration.
# If the result of the callback function is True, the element should go into the first list (i.e. the "truthy" list).
# If the result of the callback function is False, the element should go into the second list (i.e. the "falsey" list).
# When it's finished, partition should return both lists inside of one larger list, like so: [truthy_list, falsy_list]

def partition(lista, callback):
    return [[lista[i] for i in range(0, len(lista)) if callback(lista[i])], [lista[i] for i in range(0, len(lista)) if not callback(lista[i])]]
