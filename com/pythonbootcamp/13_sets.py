# Sets
# Sets do not have duplicate values
# Elements in sets aren't ordered (like dictionaries)
# You cannot access items in a set by index
# Sets can be useful if you need to keep track of a collection of elements, but don't care of ordering and duplicates

s = {1, 2, 3, 4, 5, 5, 5}
p = {4, 5, 6, 7, 8, 9, 9}

print(s)
print(4 in s)

for thing in s:
    print(thing)

print(list(set(s)))

s.add(6)
s.remove(5)
# s.remove(10) # Keyerror doesn't happen with discard()
s.discard('a')

w = s.copy()
print(w is s)

print(s | p) # The '|' operator is union of sets
print(s & p) # The '&' operator is intersection of sets
