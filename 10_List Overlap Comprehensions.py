'''
This week’s exercise is going to be revisiting an old exercise (see Exercise 5), except require the solution in
a different way.

Take two lists, say for example these two:

	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are common between the lists
(without duplicates).
Make sure your program works on two lists of different sizes. Write this in one line of Python using at least one
list comprehension.
(Hint: Remember list comprehensions from Exercise 7).

The original formulation of this exercise said to write the solution using one line of Python,
but a few readers pointed out that this was impossible to do without using sets that I had not yet discussed on
the blog, so you can either choose to use the original directive and read about the set command in Python 3.3,
or try to implement this on your own and use at least one list comprehension in the solution.

Extra:

    Randomly generate two lists to test this
'''


from random import randint


def random_list_generator(max_list_length = 99, max_value_of_element = 99):
    random_list_lenghth = randint(1, max_list_length)
    return [randint(1, max_value_of_element) for each_element in range(1, random_list_lenghth)]


def common_elements_list_generator(list_1, list_2):
    output = []

    output = [
              element_from_list_2
              for element_from_list_1 in list_1 for element_from_list_2 in list_2
              if element_from_list_1 == element_from_list_2
              ]

    return list(dict.fromkeys(output))   # removing duplicates by generating a dictionary


# >>>>>>>>>>>>>>>>>>> MAIN <<<<<<<<<<<<<<<<<<<<<


print("------------------------------------------------")
print("program that returns a list that contains only the elements that are common between the random generated lists")
list_1 = random_list_generator()
list_2 = random_list_generator()
print("first list {}".format(list_1))
print("second list {}".format(list_2))
print("common elements: {}".format(common_elements_list_generator(list_1, list_2)))
print("------------------------------------------------")

