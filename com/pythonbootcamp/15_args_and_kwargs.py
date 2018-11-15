# Parameter *args
# *args gathers remaining arguments as a tuple

def sum_all(n1, *args):
    total = 0
    print(n1)
    for n in args:
        total += n
    return total

print(sum_all(1, 2, 3, 4, 5))

lista = [1, 2, 3, 4, 5]

print(sum_all(*lista))

def ensure_login(*args):
    print(args)
    if "alex" in args and "diaz" in args:
        print("Welcome back alex diaz!")
    else:
        print("Don't know who you are...")

ensure_login("alex", "diaz")

# Parameter **kwargs
# **kwargs gathers the remaining keyword arguments as a dictionary

def fav_colors(**kwargs):
    for person, color in kwargs.items():
        print(f'{person} likes {color}')

fav_colors(alex = "red", jessie = "green", alfred = "blue")

def special_greeting(**kwargs):
    if "daniel" in kwargs and kwargs["daniel"] == "special":
        print("This is a special greeting for daniel!")
    elif "daniel" in kwargs:
        print(f"{kwargs['daniel']} daniel!")
    else:
        print("Don't know who you are..")

special_greeting(daniel = "Hello")
special_greeting(daniel = "special")

greetings = {"daniel": "Hello", "daniel": "special"}
special_greeting(**greetings)

