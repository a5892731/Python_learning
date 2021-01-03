'''
Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input),
compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

    Rock beats scissors
    Scissors beats paper
    Paper beats rock

'''
from os import system


def print_main_heading():
    print("-----------------------------------")
    print("Welcome in Rock-Paper-Scissors game")
    print("For Rock prees >>> 1 <<< ----------")
    print("For Paper prees >>> 2 <<< ---------")
    print("For Scissors prees >>> 3 <<< ------")
#----------main-----------


def solving_the_game(player_one_choice, player_two_choice, GAME_DICTIONARY):

    game_solve = ""

    if player_one_choice is player_two_choice:
        game_solve = "Draw"

    elif player_one_choice is GAME_DICTIONARY["Rock"] and player_two_choice is GAME_DICTIONARY["Paper"]:
        game_solve = "Player TWO Wins"
    elif player_one_choice is GAME_DICTIONARY["Rock"] and player_two_choice is GAME_DICTIONARY["Scissors"]:
        game_solve = "Player ONE Wins"

    elif player_one_choice is GAME_DICTIONARY["Paper"] and player_two_choice is GAME_DICTIONARY["Rock"]:
        game_solve = "Player ONE Wins"
    elif player_one_choice is GAME_DICTIONARY["Paper"] and player_two_choice is GAME_DICTIONARY["Scissors"]:
        game_solve = "Player TWO Wins"

    elif player_one_choice is GAME_DICTIONARY["Scissors"] and player_two_choice is GAME_DICTIONARY["Rock"]:
        game_solve = "Player TWO Wins"
    elif player_one_choice is GAME_DICTIONARY["Scissors"] and player_two_choice is GAME_DICTIONARY["Paper"]:
        game_solve = "Player ONE Wins"


    return game_solve



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> MAIN <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

GAME_DICTIONARY = {"Rock" : 1, "Paper" : 2, "Scissors" : 3}  # key : value

while True:
    player_one_choice = ""
    player_two_choice = ""


    print_main_heading()

    try:
        player_one_choice = int(input("\n>>> player one choice: "))
    except ValueError:
        system('cls')  # clear screen
        print(">>> >>> >>> wrong choice, please put the number")
        continue
    if player_one_choice < 1 or player_one_choice > 3:
        system('cls')  # clear screen
        print(">>> >>> >>> wrong choice, please put the correct number")
        continue


    system('cls') # clear screen

    print_main_heading()
    try:
        player_two_choice = int(input("\n>>> player two choice: "))
    except ValueError:
        system('cls')  # clear screen
        print(">>> >>> >>> wrong choice, please put the number")
        continue
    if player_two_choice < 1 or player_two_choice > 3:
        system('cls')  # clear screen
        print(">>> >>> >>> wrong choice, please put the correct number")
        continue


    system('cls')  # clear screen


    print("player one choice: {}".format(dict(map(reversed, GAME_DICTIONARY.items()))[player_one_choice])) # value : key from GAME_DICTIONARY
    print("player one choice: {}".format(dict(map(reversed, GAME_DICTIONARY.items()))[player_two_choice])) # value : key from GAME_DICTIONARY
    print("\ngame result: " + solving_the_game(player_one_choice, player_two_choice, GAME_DICTIONARY))
    print("congratulations")
    next_game_choice = input("\n>>> do you want to continue Y/N?: ")
    if next_game_choice == "y" or next_game_choice == "Y":\
        system('cls')  # clear screen
    else:
        print("exit")
        break