'''
Created on Nov 12, 2018

@author: Administrator
'''

################################### EXCERCISE 1 ###################################

# State Abbreviations Exercise
# Given two lists ["CA", "NJ", "RI"] and ["California", "New Jersey", "Rhode Island"] create a dictionary that looks like this
# {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}. Save it to a variable called answer.
# I expect you to do this with a dictionary comprehension, but you can also use a built-in function called zip.

list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
answer = { list1[i]:list2[i] for i in range(0, len(list1)) }

################################### EXCERCISE 2 ###################################

# Given a person variable:
# Create a dictionary called answer, that makes each first item in each list a key and the second item a corresponding value.
# That's a terrible explanation. I think it'll be easier if you just look at the end goal: {'name': 'Jared', 'job': 'Musician', 'city': 'Bern'}
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer2 = { person[i][0]:person[i][1] for i in range(0, len(person)) }
# { thing[0]:thing[1] for thing in person }
# { k:v for k,v in person }
# dict(person)

################################### EXCERCISE 3 ###################################

# Create a dictionary with the key as a vowel in the alphabet and the value as 0. Your dictionary should look like this {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
answer3 = { vowel:0 for vowel in 'aeiou' }
# answer = dict.fromkeys("aeiou", 0)

################################### EXCERCISE 4 ###################################

# Every character has an ASCII code (basically, a number that represents it).
# Python has a function called chr() that will return a string if you provide the corresponding integer ASCII code. For example:
# chr(65) will return 'A' chr(66) will return 'B' All the way up to: chr(90) will return 'Z'
# Your task is to create dictionary that maps ASCII keys to their corresponding letters.  Use a dictionary comprehension and chr().
# Save the result to the answer variable. You only need to care about capital letters (65-90).
# The end result will look like this: { 65:'A', 66:'B', 67:'C', 68:'D', ..., 90:'Z' }

answer4 = { i:chr(i) for i in range(65, 91) }
