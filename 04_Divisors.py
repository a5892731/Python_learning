'''
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
'''



def divisors_list_creator(number):
    return [divisor for divisor in range(1, number + 1) if number % divisor == 0]


#----------------------main---------------------
print("creating a list with all the divisors of inputed number")
print("for exit input a wrong value \n")
while True:
    try:
        input_number = int(input("input number: "))
    except ValueError:
        print("value error - end off program")
        break
    print("List of all divisors: {}".format(divisors_list_creator(input_number)))

    print("--------------loop separator--------------")