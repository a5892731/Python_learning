'''
Given two .txt files that have lists of numbers in them, find the numbers that are overlapping.
One .txt file has a list of all prime numbers under 1000,
and the other .txt file has a list of happy numbers up to 1000.

(If you forgot, prime numbers are numbers that can’t be divided by any other number.
And yes, happy numbers are a real thing in mathematics - you can look it up on Wikipedia.
The explanation is easier with an example, which I will describe below.)
'''

def list_of_primary_numbers_generator(max_value = 1000):
    def divisors_list_creator(number):
        return [divisor for divisor in range(1, number + 1) if number % divisor == 0]

    def prime_number_check(number):

        if len(divisors_list_creator(number)) == 2:  # the prime number can be divided only by 1 and himself (2 divisors)
            return True
        else:
            return False

    potential_prime_number = 2 # two is the firs prime number
    prime_numbers_list = []

    while potential_prime_number < max_value:
        if prime_number_check(potential_prime_number):
            prime_numbers_list.append(potential_prime_number)
        potential_prime_number += 1
    return prime_numbers_list

def list_of_happy_numbers_generator(max_value = 1000):

    def pdi_function(number, base: int = 10):
        """Perfect digital invariant function."""
        total = 0
        while number > 0:
            total += pow(number % base, 2)
            number = number // base
        return total

    def is_happy(number: int) -> bool:
        """Determine if the specified number is a happy number."""
        seen_numbers = set()
        while number > 1 and number not in seen_numbers:
            seen_numbers.add(number)
            number = pdi_function(number)

        return number == 1

    potential_happy_number = 1
    happy_numbers_list = []

    while potential_happy_number < max_value:
        if is_happy(potential_happy_number):
            happy_numbers_list.append(potential_happy_number)
        potential_happy_number += 1
    return happy_numbers_list

def create_file_with_list(list, file_name):
    file = open(file_name, 'w', encoding="utf-8")

    for item in list:
        print(item, file = file)

    file.close()

def read_list_from_file(file_name):
    output_list = []

    file = open(file_name, 'r', encoding="utf-8")
    for line in file:
        output_list.append(line.rstrip("\n"))

    file.close()
    return output_list

def common_elements_from_two_lists(list_1, list_2):
    common_elements = []
    for number in list_1:
            if number in list_2:
                common_elements.append(number)
    return common_elements

# >>>>>>>>>>>>>>>>>>> MAIN <<<<<<<<<<<<<<<<<<<<<

print("----------------------------------------------------------------")
print("this program finds the numbers that are overlapping in two files")

create_file_with_list(list_of_primary_numbers_generator(), "23_File Overlap - Primary numbers.txt")
create_file_with_list(list_of_happy_numbers_generator(), "23_File Overlap - Happy numbers.txt")

prime_and_happy_numbers = common_elements_from_two_lists(
    read_list_from_file("23_File Overlap - Primary numbers.txt"),
    read_list_from_file("23_File Overlap - Happy numbers.txt"))

print("Primary numbers: " + str(read_list_from_file("23_File Overlap - Primary numbers.txt")))
print("Happy numbers: " + str(read_list_from_file("23_File Overlap - Happy numbers.txt")))
print("Common elements: " + str(prime_and_happy_numbers))

create_file_with_list(prime_and_happy_numbers, "23_File Overlap - Primary&Happy numbers.txt")
