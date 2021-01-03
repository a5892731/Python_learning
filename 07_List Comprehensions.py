'''
Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
'''


# input list
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
imputed_list_a = a
#-----------

print("program that takes list a and makes a new list that has only the even elements of this list in it.")
print("list a: {}".format(imputed_list_a))
print("even elements: {}".format( [list_element for list_element in imputed_list_a if (list_element % 2 == 0)] ))

