import random

print("...rocks...")
print("...paper...")
print("...scissors...")

human = input("Player chooses: ").lower()
computer = ["rock", "paper", "scissors"][random.randint(0,2)]

print(f"Computer choice is {computer} so...")

if human == computer:
    print("It's a tie!")
elif human == "rock":
    if computer == "paper":
        print("Computer wins!")
    elif computer == "scissors":
        print("Player wins!")
elif human == "paper":
    if computer == "scissors":
        print("Computer wins!")
    elif computer == "rock":
        print("Player wins!")
elif human == "scissors":
    if computer == "rock":
        print("Computer wins!")
    elif computer == "paper":
        print("Player wins!") 
else:
    print("Something went wrong!")