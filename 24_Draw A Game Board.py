'''
This exercise is Part 1 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 2, Part 3, and Part 4.
Time for some fake graphics! Let’s say we want to draw game boards that look like this:
 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes
(8x8 for chess, 19x19 for Go, and many more).
Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.
Remember that in Python 3, printing to the screen is accomplished by
  print("Thing to show on screen")
Hint: this requires some use of functions, as were discussed previously on this blog and elsewhere on the Internet,
like this TutorialsPoint link.
http://www.tutorialspoint.com/python/python_functions.htm
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
                if row > 0 and row < (field_height - 1): # midle elements of pole
                    if x_pole != width:
                        print("|" + field_width * " ", end= "")
                    elif x_pole == width:
                        print("|", end= "")
            print() # end of line "\n"

# >>>>>>>>>>>>>>>>>>> MAIN <<<<<<<<<<<<<<<<<<<<<

drow_game_bord(3, 3, 5, 5)

print("\n" * 2)

drow_game_bord(2, 6)