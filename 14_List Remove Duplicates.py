'''
Write a program (function!) that takes a list and returns a new list that contains all the elements
of the first list minus all the duplicates.

Extras:

* Write two different functions to do this - one using a loop and constructing a list, and another using sets.
* Go back and do Exercise 5 using sets, and write the solution for that in a different function.
'''


from random import randint


def random_list_generator(max_list_length = 99, max_value_of_element = 99):
    random_list_lenghth = randint(1, max_list_length)

    return [randint(1, max_value_of_element) for each_element in range(1, random_list_lenghth)]


def duplicates_filter_in_list(inputed_list):

    return list(dict.fromkeys(inputed_list))   # removing duplicates by generating a dictionary




# >>>>>>>>>>>>>>>>>>> MAIN <<<<<<<<<<<<<<<<<<<<<


print("------------------------------------------------")
print("program that takes a list and returns a new list" +
      "that contains all the elements of the first list minus all the duplicates\n")

inputed_list = random_list_generator()
#inputed_list = [1, 1, 2, 3, 5, 5, 5, 8, 13, 21, 34, 5, 89] # test list

print("\n Inputed list {}".format(inputed_list))
print("\n>>> filtered list: {}".format(duplicates_filter_in_list(inputed_list)))
print(">>> number of elements in original list: {} and filtered list: {}".format(len(inputed_list), len(duplicates_filter_in_list(inputed_list))))
print("------------------------------------------------")

