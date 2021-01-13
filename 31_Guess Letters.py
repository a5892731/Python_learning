'''
This exercise is Part 2 of 3 of the Hangman exercise series. The other exercises are: Part 1 and Part 3.

Let’s continue building Hangman. In the game of Hangman, a clue word is given by the program that the player
has to guess, letter by letter. The player guesses one letter at a time until the entire word has been guessed.
(In the actual game, the player can only guess 6 letters incorrectly before losing).

Let’s say the word the player has to guess is “EVAPORATE”. For this exercise, write the logic that asks a player
to guess a letter and displays letters in the clue word that were guessed correctly.
For now, let the player guess an infinite number of times until they get the entire word.
As a bonus, keep track of the letters the player guessed and display a different message if the player tries
to guess that letter again. Remember to stop the game when all the letters have been guessed correctly!
Don’t worry about choosing a word randomly or keeping track of the number of guesses the player has remaining
- we will deal with those in a future exercise.

An example interaction can look like this:

#>>> Welcome to Hangman!
_ _ _ _ _ _ _ _ _
#>>> Guess your letter: S
Incorrect!
#>>> Guess your letter: E
E _ _ _ _ _ _ _ E
...
And so on, until the player gets the word.

       |||||||||||||||
       |||  ||      |
       |||||      ('_')
       |||        \ | /
       |||         ( )
       |||         / \
|||||||||||||||||


'''

from Lesson31_functions import draw_hangman

from linecache import getline
from random import randint

def file_lines_count(file_address):
    file = open(file_address, 'r')
    lines_count = 0
    for line in file:
        lines_count += 1
    file.close()
    return lines_count

def random_word_generator(file_address):
    length_of_file = file_lines_count(file_address)
    random_line_number = randint(1, length_of_file)
    random_word = getline(file_address, random_line_number)
    return random_word

def blanc_guessed_word_generator(correct_word_len):
    output = ""
    for letter in range(correct_word_len):
        output = output + "_"
    return output

def guessed_letter_check(error_count, guessed_letter, guessed_word, correct_word):

    new_guessed_word = ""

    if guessed_letter in correct_word:
        for letter_num in range(len(correct_word)):
            if guessed_letter == correct_word[letter_num]:
                new_guessed_word += guessed_letter
            else:
                new_guessed_word += guessed_word[letter_num]

        return new_guessed_word, error_count
    else:
        error_count += 1
        return guessed_word, error_count

# >>>>>>>>>>>>>>>>>>>> main <<<<<<<<<<<<<<<<<<<<<<<<



error_count = 0

guessed_letter = ""
#correct_word = random_word_generator("30_Pick Word - sowpods.txt")  # English words list
correct_word = random_word_generator("31_Pick Word - SLOWA PL.txt")  # Polish word list
correct_word = correct_word.rstrip("\n").upper()
guessed_word = blanc_guessed_word_generator(len(correct_word))


while True:

    draw_hangman(error_count)
    #print("\nCorrect word: " + correct_word )  # FOR APP TEST
    print("Your word:    " + guessed_word )
    print("Number of errors: " + str(error_count) )

    guessed_letter = input("Give me a letter: ")
    guessed_word, error_count = guessed_letter_check(error_count, guessed_letter.upper(), guessed_word, correct_word)




    if error_count >= 6:
        draw_hangman(error_count)
        print("YOU WERE HANGED!")
        print("Your word:    " + correct_word)
        break

    if "_" not in guessed_word:
        draw_hangman(error_count)
        print("YOU ARE ALIVE!")
        break