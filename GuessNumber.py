# Import the 'random' module to work with random numbers
import random

# Ask the user to input a guess
guesser = input("Guess a number: ")

# Check if the input is a digit (number)
if guesser.isdigit():
    # Convert the input to an integer
    guesser = int(guesser)

    # Check if the guess is less than or equal to 0
    if guesser <= 0:
        print("Please type a number larger than 0 next time.")
        quit()  # Quit the program
else:
    print("Please type a number larger than 0 next time.")
    quit()  # Quit the program

# Generate a random number between 0 and 5
random_number = random.randint(0, 5)
guesses = 0

# Start a loop for the guessing game
while True:
    guesses += 1
    # Ask the user to make a guess
    user_guess = input("Make a guess: ")

    # Check if the user's input is a digit (number)
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue  # Skip the rest of the loop and ask for a new guess

    # Compare the user's guess with the random number
    if user_guess == random_number:
        print("You got it right!")  # Print a success message
        break  # Exit the loop, the game is won
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the nunber!")

print(f" You got it in {guesses} guesses")
