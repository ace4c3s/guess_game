import random


def guess_game():

    random_number = random.randint(1,100)

    print("Welcome to the Guessing Game")
    total_guesses = 0

    while True:
        guess = int(input("Guess the number: "))
        total_guesses += 1

        if total_guesses == 3:
           print("You have 3 attempts only, restart the game!")
           break

        if guess > random_number:
         print("Too high, try again.")

        elif guess < random_number:
            print("Too low, try again")

        else:
            print(f"Yah. You guessed number {guess} correctly. ")
            print(f"It took you {total_guesses} attempts to guess the correct number.")
            break

guess_game()