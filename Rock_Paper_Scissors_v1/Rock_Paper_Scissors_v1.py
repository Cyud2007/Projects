from ast import main
import random 

user_item = input("Make your choice - stone/paper/scissors: ")
possible_actions = ["stone", "paper", "scissors"]
computer_action = random.choice(possible_actions)
print(f"\nYou have selected - {user_item}, the computer has selected - {computer_action}.\n")
if user_item == computer_action:
    print(f"Both players chose - {user_item}. Draw!")
elif user_item == "stone":
    if computer_action == "scissors":
        print("Stone beats scissors! You won!")
    else:
        print("Paper wraps stone! You lose.")
elif user_item == "paper":
    if computer_action == "stone":
        print("Paper wraps stone! You won!")
    else:
        print("Scissors cut paper! You lose.")
elif user_item == "scissors":
    if computer_action == "paper":
        print("Scissors cut paper! You won!")
    else:
        print("Stone beats scissors! You lose.")