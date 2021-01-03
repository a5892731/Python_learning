'''
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
(Hint: remember to use the user input lessons from the very first exercise)

Extras:

    Keep the game going until the user types “exit”
    Keep track of how many guesses the user has taken, and when the game ends, print this out.

'''

from random import randint


# >>>>>>>>>>>>>>>>>>>>>>> MAIN <<<<<<<<<<<<<<<<<<<<<<<<<<



while True:

    guesses = 1
    random_number = randint(1, 9)

    while True:



        print("guess the number from 1 to 9")
        try:
            user_guess = int(input(">>> "))
        except ValueError:
            print("wrong data")
        if user_guess < 1 or user_guess > 9:
            print("data out of range")
        elif user_guess < random_number:
            print("wrong gues, too low")
        elif user_guess > random_number:
            print("wrong gues, too high")
        elif user_guess == random_number:
            print("NICE! Exactly right")
            print("You finished at {} attempt".format(guesses))
            break

        guesses += 1

    next_game_choice = input("\n>>> do you want to continue Y/N?: ")
    if next_game_choice == "y" or next_game_choice == "Y":
        continue
    else:
        print("exit")
        break