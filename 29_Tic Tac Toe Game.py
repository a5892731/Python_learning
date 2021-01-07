'''
This exercise is Part 4 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 1, Part 2, and Part 3.

In 3 previous exercises, we built up a few components needed to build a Tic Tac Toe game in Python:

Draw the Tic Tac Toe game board
Checking whether a game board has a winner
Handle a player move from user input
The next step is to put all these three components together to make a two-player Tic Tac Toe game! Your challenge in this exercise is to use the functions from those previous exercises all together in the same program to make a two-player game that you can play with a friend. There are a lot of choices you will have to make when completing this exercise, so you can go as far or as little as you want with it.

Here are a few things to keep in mind:

You should keep track of who won - if there is a winner, show a congratulatory message on the screen.
If there are no more moves left, don’t ask for the next player’s move!
As a bonus, you can ask the players if they want to play again and keep a running tally of who won more - Player 1 or Player 2.
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

def switch_tic_tac_toe_player(previouse_player):
    if previouse_player == "X":
        return "O"
    elif previouse_player == "O":
        return "X"
    else:
        return False

def tic_tac_toe_mechanizm(adres, player, game_values, occupied_poles = 0):
    COLUMNS_DICTIONARY = {"A": 0, "B": 1, "C": 2, "D": 3,"E": 4, "F": 5, "G": 6, "H": 7, "I": 8}
    ROWS_DICTIONARY = {"1": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8}
    #adres example: A1 whehe A is column and 1 row
    #player is O or X
    #game values is board matrix
    #occupied_poles is number or previouse moves
    column = COLUMNS_DICTIONARY[adres[0]] #first sign
    row = ROWS_DICTIONARY[adres[1]] #second sign

    if game_values[row][column] == "O" or game_values[row][column] == "X":
        return game_values, player, occupied_poles  # when target is occupied field > do nothing
    else:
        game_values[row][column] = player
        occupied_poles += 1
        return game_values, switch_tic_tac_toe_player(player), occupied_poles # change object and switch player



# >>>>>>>>>>>>>>>>>>> MAIN <<<<<<<<<<<<<<<<<<<<<

square_size = 3


while True: # games loop
    current_player = "O"  # "O" start the game
    occupied_poles = 0

    game_values = [["1", "1", "1"],
                   ["2", "2", "2"],
                   ["3", "3", "3"]]


    while True: # game loop
        print(" ----------- ")
        print(" TIC TAC TOE:")
        print(" --- --- --- ")
        print("  A   B   C  ")
        drow_game_bord(game_values, square_size, square_size)
        print("Player {} turn.".format(current_player))
        print("Choice place. For example A1")
        player_choice = input("Your choice: >>> {} <<< : ".format(current_player))
        player_choice = player_choice.capitalize()
        print("Your choice is: {}".format(player_choice))


        [game_values, current_player, occupied_poles] = tic_tac_toe_mechanizm(player_choice,
                                                                                           current_player,
                                                                                           game_values,
                                                                                           occupied_poles)


        x_status = tic_tac_toe_game_result(game_values, "X")
        o_status = tic_tac_toe_game_result(game_values, "O")

        if x_status == True or o_status == True or occupied_poles == pow(square_size, 2):
            drow_game_bord(game_values)
            if occupied_poles == pow(square_size, 2):
                print("DRAW: All poles are occupied")
            break

    next_game_choice = input("\n>>> do you want to play again? Y/N: ")
    if next_game_choice == "y" or next_game_choice == "Y":
        continue
    else:
        print("exit")
        break