'''
Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

and write a program that prints out all the elements of the list that are less than 5.

Extras:

    Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
    Write this in one line of Python.
    Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

'''

list_of_numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def list_less_than_number(list, number):
    return [list_element for list_element in list if list_element < number]


for number in list_of_numbers:
    if number < 5:
        print(number)

print("----------------- new solution -----------------")


#list_of_nubers_that_are_lesss_tham_5 = [number for number in list_of_numbers if number < 5]
print("list of numbers smaller than 5")
print(list_less_than_number(list_of_numbers, 5))

print("----------------- new solution -----------------")

number = int(input("Paste a number: "))
print("list of numbers smaller than {}".format(number))
print(list_less_than_number(list_of_numbers, number))