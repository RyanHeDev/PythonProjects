import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

# This loop continues until the user decides to quit
while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue
    random_number = random.randint(0, 2)
    # Convert random number to a choice from options
    computer_pick = options[random_number]
    print(f"Computer picked {computer_pick}.")

    # Determine the winner based on choices
    if user_input == "rock" and computer_pick == options[2]:
        print("You won!")
        user_wins += 1
    elif user_input == "paper" and computer_pick == options[0]:
        print("You won!")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == options[1]:
        print("You won!")
        user_wins += 1
    elif user_input == computer_pick:
        print("Draw")
    else:
        print("You lost!")
        computer_wins += 1

    # Check if either player has reached 3 wins
    if user_wins == 3 or computer_wins == 3:
        print(f"Your score is {user_wins}")
        print(f"The computer score is {computer_wins}")
        break

# End the game
print("Goodbye")
