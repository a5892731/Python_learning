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

def drow_game_bord(height = 3, width = 3, field_height = 3, field_width = 3):

    #y_pole is actual pole number in y axix
    #x_pole is actual pole number in x axis

    for y_pole in range(height):
        for row in range(field_height):
            for x_pole in range(width + 1):  # extra "1" is for generating end in last pole
                if row == 0 or row == (field_height - 1): # up and down elements of pole
                    if x_pole != width:
                        print(" " + field_width * "-", end= "")
                    elif x_pole == width:
                        print(" ", end= "")
                if row > 0 and row < (field_height - 1): # middle elements of pole
                    if x_pole != width:
                        print("|" + field_width * " ", end= "")
                    elif x_pole == width:
                        print("|", end= "")
            print() # end of line "\n"

# >>>>>>>>>>>>>>>>>>> MAIN <<<<<<<<<<<<<<<<<<<<<


drow_game_bord()