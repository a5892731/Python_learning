'''
Write a program (using functions!) that asks the user for a long string containing multiple words.
Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

  My name is Michele
Then I would see the string:

  Michele is name My
shown back to me.
'''




def backwards_string_generator(string):

    list_of_words = string.split()
    output = ""

    for word in list_of_words[::-1]:
        output = output + word + " "

    return output.rstrip(" ")

# >>>>>>>>>>>>>>>>>>> MAIN <<<<<<<<<<<<<<<<<<<<<


print("------------------------------------------------")
print("program that print words from imputed string in backwards order ")
string_from_user = input("give me your string: ")

print("\n>>> you backwards string: {}".format(backwards_string_generator(string_from_user)))
