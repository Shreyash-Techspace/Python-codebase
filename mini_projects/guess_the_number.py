"""
Create a simple number guessing game
The user gets 10 chances to guess the number
If the user guesses the number before 10 chances, stop asking the number from the user, say Congrats and end the game
If the user never guesses the number, ask them 10 times and end the game
"""

import random

num = 1
print("Welcome to the number guessing game")
print("We have a number that need to be guessed and you have a 10 attempts")
print("The Secret number is between 1 and 50")

secret_number = random.randint(1, 50)
attempts = 10
is_guess_correct = False

while num <= 10:
    print(f"You have {attempts} attempts remaining to guess the number")
    user_number = int(input("Enter your guess: "))
    if user_number == secret_number:
        print(f"You guessed the correct number")
        is_guess_correct = True
        break
    else:
        if user_number < secret_number:
            higher_or_lower = "higher"
        else:
            higher_or_lower = "lower"
        print(f"Your guess is wrong! Try {higher_or_lower} number.")

    num = num + 1
    attempts = attempts + 1

if not is_guess_correct:
    print("Bad luck!! You exhausted all your attempts and couldn't guess the number")

print(f"The secret number was {secret_number}. GAME OVER !!")
