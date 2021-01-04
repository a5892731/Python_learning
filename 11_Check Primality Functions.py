'''
Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten,
a prime number is a number that has no divisors.).
You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions,
described below.
'''




def divisors_list_creator(number):
    return [divisor for divisor in range(1, number + 1) if number % divisor == 0]

def prime_number_check(number):

    if len(divisors_list_creator(number)) == 2: #the prime number can be divided only by 1 and himself (2 divisors)
        return ">>> this number is prime"
    else:
        return ">>> this number is not prime!"


# >>>>>>>>>>>>>>>>>>> MAIN <<<<<<<<<<<<<<<<<<<<<


print("------------------------------------------------")
print("program that ask the user for a number and determine whether the number is prime or not ")
try:
    number_from_user = int(input("so give me a number: "))
    print(prime_number_check(number_from_user))
except ValueError:
    print(">>> that was not integer number!")