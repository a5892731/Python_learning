'''
Given two .txt files that have lists of numbers in them, find the numbers that are overlapping.
One .txt file has a list of all prime numbers under 1000,
and the other .txt file has a list of happy numbers up to 1000.

(If you forgot, prime numbers are numbers that can’t be divided by any other number.
And yes, happy numbers are a real thing in mathematics - you can look it up on Wikipedia.
The explanation is easier with an example, which I will describe below.)
'''


from random import randint



def random_list_generator(list_length = 1000, max_value_of_element = 1000):
    return [randint(1, max_value_of_element) for each_element in range(list_length)]

def happy_numbers_generator(max_value = 1000):
    None

def create_list_of_primary_numbers(max_value = 1000):
    def divisors_list_creator(number):
        return [divisor for divisor in range(1, number + 1) if number % divisor == 0]

    def prime_number_check(number):

        if len(divisors_list_creator(
                number)) == 2:  # the prime number can be divided only by 1 and himself (2 divisors)
            return True
        else:
            return False

    potential_prime_number = 3
    prime_numbers_list = []

    while potential_prime_number < max_value:
        if prime_number_check(potential_prime_number):
            prime_numbers_list.append(potential_prime_number)
        potential_prime_number += 1
    return prime_numbers_list

def create_file_with_list(list, file_name):
    file = open(file_name, 'w', encoding="utf-8")

    for item in list:
        print(item, file = file)

    file.close()

def read_list_from_file(file_name):
    output_list = []

    file = open(file_name, 'r', encoding="utf-8")
    for line in file:
        output_list.append(line)

    file.close()
    return output_list




# >>>>>>>>>>>>>>>>>>> MAIN <<<<<<<<<<<<<<<<<<<<<

print("----------------------------------------------------------------")
print("this program finds the numbers that are overlapping in two files")

#create_file_with_list(random_list_generator(), "23_File Overlap - Random numbers.txt")
create_file_with_list(create_list_of_primary_numbers(), "23_File Overlap - Primary numbers.txt")


