'''
This exercise is Part 3 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 1, Part 2, and Part 4.

In a previous exercise we explored the idea of using a list of lists as a “data structure” to store information about
a tic tac toe game. In a tic tac toe game, the “game server” needs to know where the Xs and Os are in the board,
to know whether player 1 or player 2 (or whoever is X and O won).

There has also been an exercise about drawing the actual tic tac toe gameboard using text characters.

The next logical step is to deal with handling user input. When a player (say player 1, who is X)
wants to place an X on the screen, they can’t just click on a terminal. So we are going to approximate this clicking
simply by asking the user for a coordinate of where they want to place their piece.

As a reminder, our tic tac toe game is really a list of lists. The game starts out with an empty game board like this:

game = [[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]
The computer asks Player 1 (X) what their move is (in the format row,col), and say they type 1,3.
Then the game would print out

game = [[0, 0, X],
	[0, 0, 0],
	[0, 0, 0]]
And ask Player 2 for their move, printing an O in that place.

Things to note:

For this exercise, assume that player 1 (the first player to move) will always be X and player 2
(the second player) will always be O.
Notice how in the example I gave coordinates for where I want to move starting from (1, 1) instead of (0, 0).
To people who don’t program, starting to count at 0 is a strange concept, so it is better for the user experience
if the row counts and column counts start at 1. This is not required, but whichever way you choose to implement this,
it should be explained to the player.
Ask the user to enter coordinates in the form “row,col” - a number, then a comma, then a number.
Then you can use your Python skills to figure out which row and column they want their piece to be in.
Don’t worry about checking whether someone won the game, but if a player tries to put a piece in a game position
where there already is another piece, do not allow the piece to go there.
Bonus:

For the “standard” exercise, don’t worry about “ending” the game - no need to keep track of how many squares are full.
In a bonus version, keep track of how many squares are full and automatically stop asking for moves when there
are no more valid moves.
'''


def drow_game_bord(inpur_values = [], height = 3, width = 3, field_height = 3, field_width = 3):

    #y_pole is actual pole number in y axix
    #x_pole is actual pole number in x axis
    #field_width and height must be odd
    #input values matrix must fit in heigh and width of board


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
                        if row == ((field_height - 1) / 2): # input value mus be in center of pole
                            print("|" + int((field_width - 1)/2) * " " +
                                  inpur_values[y_pole][x_pole] +
                                  int((field_width - 1)/2) * " ", end= "")
                        else:
                            print("|" + field_width * " " , end="")
                    elif x_pole == width:
                        print("|", end= "")
            print() # end of line "\n"

def tic_tac_toe_game_result(game_values, player, square_range = 3): # player must be named O or X
    game_result = False

    if game_result == False:  # possible win in columns check
        column = 0
        while column < square_range:
            row = 0
            while row < square_range:
                if game_values[row][column] == player:
                    game_result = True
                else:
                    game_result = False
                    break
                row += 1
            column += 1
            if game_result == True:
                print(">>> {} in COLUMN WON".format(player))
                break

    if game_result == False:  # possible win in rows check
        row = 0
        while row < square_range:
            column = 0
            while column < square_range:
                if game_values[row][column] == player:
                    game_result = True
                else:
                    game_result = False
                    break
                column += 1
            row += 1
            if game_result == True:
                print(">>> {} in ROW WON".format(player))
                break

    if game_result == False: # possible win in first diagonal check
        diagonal = 0

        while diagonal < square_range:
            if game_values[diagonal][diagonal] == player:
                game_result = True
            else:
                game_result = False
                break
            diagonal += 1
        if game_result == True:
            print(">>> {} in DIAGONAL WON".format(player))

    if game_result == False: # possible win in second diagonal check
        diagonal = 0
        while diagonal < square_range:
            if game_values[-(diagonal + 1)][diagonal] == player:
                game_result = True
            else:
                game_result = False
                break
            diagonal += 1
        if game_result == True:
            print(">>> {} in DIAGONAL WON".format(player))

    return game_result

# >>>>>>>>>>>>>>>>>>> MAIN <<<<<<<<<<<<<<<<<<<<<

TIC_TAC_TOE_DICTIONARY = {"O" : 1, "X" : 2 }
o_x_switch = "O" # "O" start the game

game_values = [["3", "3", "3"],
               ["2", "2", "2"],
               ["1", "1", "1"]]

game_values = [["X", "3", "3"],
               ["2", "X", "2"],
               ["1", "1", "X"]]

print(" ----------- ")
print(" TIC TAC TOE:")
print(" --- --- --- ")
print("  A   B   C  ")
drow_game_bord(game_values)

#player_choice = input("Choice place for >>> {} <<< : ".format(o_x_switch))
#player_choice = player_choice.capitalize()
#print("Your choice is: {}".format(player_choice))

x_status = tic_tac_toe_game_result(game_values, "X")
o_status = tic_tac_toe_game_result(game_values, "O")
