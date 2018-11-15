# FIRST EXERCISE

# Your task is to simply print out a string depending on if food  is a value in bakery_stock.
# If food  is contained in bakery_stock print out a string that states how many items are left: "3 left" if food is "toffee cookie"
# or "1 left" if food  is "morning bun", etc.

from random import choice
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"])

bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

if food in bakery_stock:
    print(bakery_stock.get(food) + "left")
else:
    print("We don't make that")

# SECOND EXERCISE

# Use the game_properties list and dict.fromkeys() to generate a dictionary with all values set to 0.  Save the result to a variabled called initial_game_state
game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notications", "achievements"] 

initial_game_state = dict.fromkeys(game_properties, 0)
