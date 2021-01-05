'''
Create a program that will play the “cows and bulls” game with the user. The game works like this:

Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.

Say the number generated by the computer is 1038. An example interaction could look like this:

  Welcome to the Cows and Bulls Game!
  Enter a number:
  #>>> 1234
  2 cows, 0 bulls
  #>>> 1256
  1 cow, 1 bull
  ...
    Until the user guesses the number.
'''


from random import randint


def x_digit_number_generator(x = 4, min_digit_value = 0, max_digit_value = 9): #where x is number of segments
    return [str(randint(min_digit_value, max_digit_value)) for digit_segment in range(x)]

def string_from_list_generator(list):
    output = ""
    for element in list:
        output += str(element)
    return output

def string_to_list_generator(string):
    output_list = []
    output_list[:] = string
    return output_list

def list_comparator_for_cow_and_bull_game(list_1, list_2):
    cow = 0
    bull  = 0
    for iteration in range(len(list_1)):
        if list_1[iteration] == list_2[iteration]:
            cow += 1
        else:
            bull += 1
    return [cow, bull]





# >>>>>>>>>>>>>>>>>>> MAIN <<<<<<<<<<<<<<<<<<<<<


random_4_digit_number = x_digit_number_generator()
number_of_cows = 0
number_of_bulls = 0
attempt = 1

print("------------------------------------------")
print("this is cows and bulls game!--------------")
print("guessed the {} numbers in the correct order".format(len(random_4_digit_number)))


while True:
    guessing_number = input("\n>>> guess the {} digit: ".format(len(random_4_digit_number)))
    try:
        [number_of_cows, number_of_bulls] = list_comparator_for_cow_and_bull_game(random_4_digit_number, string_to_list_generator(guessing_number))
    except IndexError:
        continue
    print("\n{} cows, {} bulls".format(number_of_cows, number_of_bulls))

    if number_of_cows == len(random_4_digit_number):
        break
    else:
        print("\ntry again")
        attempt += 1

print("\nrandom number is: {}".format(string_from_list_generator(random_4_digit_number)))
print("your score: {} cows and {} bulls at {} attempt".format(number_of_cows, number_of_bulls, attempt))

