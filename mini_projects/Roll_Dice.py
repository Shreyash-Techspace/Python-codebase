import random

print("Welcome to the Game of Rolling a Dice ")

while True:
    choice = input("Press 'Enter' if you want to roll a dice or You can Quit by Pressing a 'q' ")
    choice = choice.strip()

    if choice == 'q':
        print("Thanks for playing the game ")
        break
    elif choice == '':
        c = random.randint(1, 6)
        print(f"Your number is {c}")
    else:
        print("Invalid Choice")
print("GAME OVER")
