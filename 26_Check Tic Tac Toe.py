'''
Exercise 26 (and Solution)
This exercise is Part 2 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 1, Part 3, and Part 4.

As you may have guessed, we are trying to build up to a full tic-tac-toe board. However, this is significantly more than half an hour of coding, so we’re doing it in pieces.

Today, we will simply focus on checking whether someone has WON a game of Tic Tac Toe, not worrying about how the moves were made.

If a game of Tic Tac Toe is represented as a list of lists, like so:

game =
   [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]
where a 0 means an empty square, a 1 means that player 1 put their token in that space, and a 2 means that player
2 put their token in that space.

Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board, tell me whether anyone
has won, and tell me which player won, if any. A Tic Tac Toe win is 3 in a row - either in a row, a column,
or a diagonal. Don’t worry about the case where TWO people have won
- assume that in every board there will only be one winner.

Here are some more examples to work with:

winner_is_2 =
   [[2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_1 =
   [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_also_1 =
   [[0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]

no_winner =
   [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]

also_no_winner =
   [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]]
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
print(x_status, o_status)

print("  A   B   C   D ")
game_values = [["4", "4", "O", "4"],
               ["3", "3", "O", "3"],
               ["2", "2", "O", "2"],
               ["1", "1", "O", "1"]]

drow_game_bord(game_values, 4, 4, 5, 7)

x_status = tic_tac_toe_game_result(game_values, "X", 4)
o_status = tic_tac_toe_game_result(game_values, "O", 4)
print(x_status, o_status)