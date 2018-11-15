numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

doubled = [num * 2 for num in numbers]

print(doubled)

stringified = [str(num) for num in numbers]

print(stringified)

even_only = [num for num in numbers if num % 2 == 0]

print(even_only)

double_odds_triple_evens = [num * 2 if num % 2 != 0 else num * 3 for num in numbers]

print(double_odds_triple_evens)

############# EXERCISES #############

# Given a list ["Elie", "Tim", "Matt"], create a variable called answer, which is a new list containing the first letter of each name in the list.
# Given a list [1,2,3,4,5,6], create a new variable called answer2, which is a new list of all the even values.

names = ["Elie", "Tim", "Matt"]
numbers = [1, 2, 3, 4, 5, 6]

answer = [name[0] for name in names]

answer2 = [n for n in numbers if n % 2 == 0]

# 1. Given two lists [1,2,3,4] and [3,4,5,6] create a variable called answer, which is a new list that is the intersection of the two.
# Your output should be [3,4]. Hint: use the in operator to test whether an element is in a list.
# 2. Given a list of words ["Elie", "Tim", "Matt"] create a variable called answer2, which is a new list with each word reversed
# and in lower case (use a slice to do the reversal!) Your output should be ['eile', 'mit', 'ttam']

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

names = ["Elie", "Tim", "Matt"]

answer = [n for n in list1 if n in list1 and n in list2]

answer2 = [name[::-1].lower() for name in names]

