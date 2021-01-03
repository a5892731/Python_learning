'''
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

    If the number is a multiple of 4, print out a different message.
    Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

'''



while True:

    try:
        number_fron_user  = int(input("Imput a number: "))
        divide_number = int(input("Imput a divide number: "))
    except ValueError:
        print("value error - end off program")
        break

    if number_fron_user % divide_number == 0:
        print(">>> This number can be divided by " + str(divide_number))
    else:
        print(">>> This number can't be divided by " + str(divide_number))
        if number_fron_user % 4 == 0:
            print(">>> >>> This number can be divided by 4")
        elif number_fron_user % 2 == 0:
            print(">>> >>> This number i even")
        elif number_fron_user % 2 > 0:
            print(">>> >>> This number is odd")

    print("-----loop separator-----")