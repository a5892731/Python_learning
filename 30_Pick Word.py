'''
This exercise is Part 1 of 3 of the Hangman exercise series. The other exercises are: Part 2 and Part 3.

In this exercise, the task is to write a function that picks a random word from a list of words from the
SOWPODS dictionary. Download this file and save it in the same directory as your Python code.
This file is Peter Norvig’s compilation of the dictionary of words used in professional Scrabble tournaments.
Each line in the file contains a single word.

https://en.wikipedia.org/wiki/Peter_Norvig
http://norvig.com/ngrams/sowpods.txt
'''

from linecache import getline
from random import randint

def file_lines_count(file_address):
    file = open(file_address, 'r')
    lines_count = 0
    for line in file:
        lines_count += 1
    file.close()
    return lines_count



# >>>>>>>>>>>>>>>>>>>> main <<<<<<<<<<<<<<<<<<<<<<<<
file_address = "30_Pick Word - sowpods.txt"
length_of_file = file_lines_count(file_address)
random_line_number = randint(1, length_of_file)

print("\nfile: " + file_address + "\n")
print("Random word: " + str(getline(file_address, random_line_number)) +
      "from row " + str(random_line_number) + " of " +str(length_of_file))
