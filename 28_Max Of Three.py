'''
Implement a function that takes as input three variables, and returns the largest of the three.
Do this without using the Python max() function!

The goal of this exercise is to think about some internals that Python normally takes care of for us.
All you need is some variables and if statements!
'''



first_number = int(input("Insert a first number: "))
second_number = int(input("Insert a second number: "))
third_number = int(input("Insert a third number: "))


print("your max is: {}".format(max(first_number, second_number, third_number))) # what is if for?