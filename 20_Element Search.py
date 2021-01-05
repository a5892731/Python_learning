'''
Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest)
 and another number. The function decides whether or not the given number is inside the list and returns (then prints)
 an appropriate boolean.

Extras:

Use binary search.
'''

from random import randint


def random_list_generator(max_list_length = 99, max_value_of_element = 99):
    random_list_lenghth = randint(1, max_list_length)

    return [randint(1, max_value_of_element) for each_element in range(1, random_list_lenghth)]

def duplicates_filter_in_list(inputed_list):

    return list(dict.fromkeys(inputed_list))   # removing duplicates by generating a dictionary


def check_if_the_nubmer_is_in_the_list(number, list):

    if number in list:
        return True
    else:
        return False






# >>>>>>>>>>>>>>>>>>> MAIN <<<<<<<<<<<<<<<<<<<<<

random_list = duplicates_filter_in_list(random_list_generator())
random_list.sort()


number_from_user = int(input("give me a number: "))


print("\n>>> is the number in the list?: {} ".format(check_if_the_nubmer_is_in_the_list(number_from_user, random_list)))

print("\nour list: {}".format(random_list))
print("our number: {}".format(number_from_user))
