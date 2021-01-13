'''
This exercise is Part 3 of 3 of the Hangman exercise series. The other exercises are: Part 1 and Part 2.

You can start your Python journey anywhere, but to finish this exercise you will have to have finished
Parts 1 and 2 or use the solutions (Part 1 and Part 2).

In this exercise, we will finish building Hangman. In the game of Hangman, the player only has 6 incorrect guesses
(head, body, 2 legs, and 2 arms) before they lose the game.

In Part 1, we loaded a random word list and picked a word from it. In Part 2, we wrote the logic for guessing the
letter and displaying that information to the user. In this exercise, we have to put it all together and add logic for
handling guesses.

Copy your code from Parts 1 and 2 into a new file as a starting point. Now add the following features:

Only let the user guess 6 times, and tell the user how many guesses they have left.
Keep track of the letters the user guessed. If the user guesses a letter they already guessed,
don’t penalize them - let them guess again.
Optional additions:

When the player wins or loses, let them start a new game.
Rather than telling the user "You have 4 incorrect guesses left", display some picture art for the Hangman.
This is challenging - do the other parts of the exercise first!
Your solution will be a lot cleaner if you make use of functions to help you!
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

def guessed_letter_check(error_count, correrct_answer_count, guessed_letter, guessed_word, correct_word):

    new_guessed_word = ""

    if guessed_letter in correct_word:
        for letter_num in range(len(correct_word)):
            if guessed_letter == correct_word[letter_num]:
                new_guessed_word += guessed_letter
                correrct_answer_count += 1
            else:
                new_guessed_word += guessed_word[letter_num]

        return new_guessed_word, error_count, correrct_answer_count
    else:
        error_count += 1
        return guessed_word, error_count, correrct_answer_count

# >>>>>>>>>>>>>>>>>>>> main <<<<<<<<<<<<<<<<<<<<<<<<


MAX_ATTEMPTS = 6
error_count = 0
correrct_answer_count = 0

guessed_letter = ""
guessed_letters_bufor = ""

#correct_word = random_word_generator("30_Pick Word - sowpods.txt")  # English words list
correct_word = random_word_generator("31_Pick Word - SLOWA PL.txt")  # Polish word list
correct_word = correct_word.rstrip("\n").upper()
guessed_word = blanc_guessed_word_generator(len(correct_word))


while True:

    draw_hangman(error_count)
    #print("\nCorrect word: " + correct_word )  # FOR APP TEST
    print("Your word:    " + guessed_word )


    guessed_letter = input("Give me a letter: ")


    if guessed_letter.upper() in guessed_letters_bufor:
        print("\nYou already used this letter!")
    else:
        guessed_letters_bufor += guessed_letter.upper()
        guessed_word, error_count, correrct_answer_count = guessed_letter_check(error_count, correrct_answer_count,
                                                           guessed_letter.upper(), guessed_word, correct_word)


    print("\nYur score = correct {}, errors {}, attemts left {}".format(correrct_answer_count, error_count,
                                                                      (MAX_ATTEMPTS - error_count)))



    if error_count >= MAX_ATTEMPTS:
        draw_hangman(error_count)
        print("YOU WERE HANGED!")
        print("Your word:    " + correct_word)
        break

    if "_" not in guessed_word:
        draw_hangman(error_count)
        print("YOU ARE ALIVE!")
        break