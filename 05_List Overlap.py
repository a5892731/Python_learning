'''
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extras:

    Randomly generate two lists to test this
    Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

'''

from random import randint


#-----------------defined input
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#------------------------------

def random_list_generator(max_list_length = 99, max_value_of_element = 99):
    random_list_lenghth = randint(1, max_list_length)
    return [randint(1, max_value_of_element) for each_element in range(1, random_list_lenghth)]


def common_elements_list_generator(list_1, list_2):
    output = []

    for element_from_list_1 in list_1:
        for element_from_list_2 in list_2:
            try:
                if element_from_list_1 == element_from_list_2 and element_from_list_2 != output[-1]:
                    output.append(element_from_list_2)

            except IndexError:
                output.append(element_from_list_2)

    return output



# main
print("------------------------------------------------")
print("program that returns a list that contains only the elements that are common between the two lists")
print("first list {}".format(a))
print("second list {}".format(b))
print("common elements: {}".format(common_elements_list_generator(a, b)))
print("------------------------------------------------")


print("second task")


print("------------------------------------------------")
print("program that returns a list that contains only the elements that are common between the random generated lists")
list_1 = random_list_generator()
list_2 = random_list_generator()
print("first list {}".format(list_1))
print("second list {}".format(list_2))
print("common elements: {}".format(common_elements_list_generator(list_1, list_2)))
print("------------------------------------------------")


print("third task")


print("------------------------------------------------")
print("program that returns a list that contains only the elements that are common between the random generated lists")
list_1 = random_list_generator()
list_2 = random_list_generator()
print("first list {}".format(list_1))
print("second list {}".format(list_2))

print("common elements: {}".format(set(list_1) & set(list_2))) # output format = tupla

print("------------------------------------------------")