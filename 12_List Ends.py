'''
Write a program that takes a list of numbers
(for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list.
For practice, write this code inside a function.
'''

#-----------------INPUT------------------
a = [5, 10, 15, 20, 25]
input_list_a = a
#----------------------------------------

def list_of_first_and_lats_element_generator(input_list):
    try:
        return [input_list[0], input_list[-1]]
    except IndexError:
        print(">>> list index out of range")

#-----------------MAIN------------------

print("------------------------------------------------")
print("program that makes a list of only the first and last elements of the given list")

print("\n>>> inputed list: {}".format(input_list_a))
print("\n>>> first and last element of this list: {}".format(list_of_first_and_lats_element_generator(input_list_a)))
