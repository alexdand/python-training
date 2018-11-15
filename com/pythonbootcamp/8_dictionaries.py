# dictionaries methods: clear, copy, fromkeys, get

new_user = {}.fromkeys(['name', 'score', 'email', 'profile'], 'unknown')  # also dict.fromkeys()
print(new_user)

other_user = {}.fromkeys('abc', 'letter')
print(other_user)

print(new_user.get('name'))

# more methods: pop, popitems, update

new_user.pop('name')
print('name' in new_user)

# new_user.pop('lastname') # keyerror
random = new_user.popitem()  # pops a random item
print(random)

# update
first = dict(a = 1, b = 2, c = 3, d = 4, e = 5)
second = {}

second.update(first)
print(second)

second['a'] = "something else"

second.update(first)
print(second)

new_user.update({'lastname': "geoffrey"})
print(new_user)
new_user["favoritefood"] = "potatoes"
print(new_user)
