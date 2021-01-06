'''
In a previous exercise, we’ve written a program that “knows” a number and asks a user to guess it.

This time, we’re going to do exactly the opposite. You, the user, will have in your head a number between 0 and 100.
The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.

At the end of this exchange, your program should print out how many guesses it took to get your number.

As the writer of this program, you will have to choose how your program will strategically guess.
A naive strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.) until you hit the number.
But that’s not an optimal guessing strategy. An alternate strategy might be to guess 50 (
right in the middle of the range), and then increase / decrease by 1 as needed. After you’ve written the program,
try to find the optimal strategy! (We’ll talk about what is the optimal one next week with the solution.)
'''

from random import randint

# >>>>>>>>>>>>>>>>>>> MAIN <<<<<<<<<<<<<<<<<<<<<

print("------------------------------------")
print("program that is guessing a number!!!")

attempt = 1
min_value = 0
max_value = 100

while True:
    guest_number = randint(min_value, max_value)

    print("This is your number?: {}".format(guest_number))
    user_response = input("put Y or N answer: ")

    if user_response == "Y" or user_response == "y":
        print("YEAH! I did it in {} attepmt!".format(attempt))
        break

    attempt += 1
    print("Your number was LOWER or HIGHER?")
    user_response = input("put H or L answer: ")
    if user_response == "H" or user_response == "h":
        min_value = guest_number + 1
    elif user_response == "L" or user_response == "l":
        max_value = guest_number - 1


