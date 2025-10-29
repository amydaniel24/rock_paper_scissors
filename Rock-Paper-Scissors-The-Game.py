
import random

OPTIONS = ["rock", "paper", "scissors"]

# everything in one cell so input() definitely runs before the checks
user_choice = input("Enter rock, paper, or scissors: ").strip().lower()

if user_choice not in OPTIONS:
    print("Invalid input. Please enter 'rock', 'paper', or 'scissors'.")
else:
    computer_choice = random.choice(OPTIONS)

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "scissors" and computer_choice == "paper")
        or (user_choice == "paper" and computer_choice == "rock")
    ):
        result = "You win!"
    else:
        result = "Computer wins!"

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(result)






