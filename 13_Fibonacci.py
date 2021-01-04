'''
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
Take this opportunity to think about how you can use functions.
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum
of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
'''


def fibonnaci_sequece_generator(length_of_fibonnaci_sequece): # https://en.wikipedia.org/wiki/Fibonacci_number


    if length_of_fibonnaci_sequece == 0:
        return [0]
    elif length_of_fibonnaci_sequece == 1:
        return [1]
    elif length_of_fibonnaci_sequece > 1:

        output_in_iteration_minus_1 = 1 # loop is starting in iteration 2!
        output_in_iteration_minus_2 = 0 # loop is starting in iteration 2!
        output = 0
        output_list = [1]

        for iteration in range(2, length_of_fibonnaci_sequece + 1):  # loop is starting in iteration 2!

            output = output_in_iteration_minus_1 + output_in_iteration_minus_2
            output_in_iteration_minus_2 = output_in_iteration_minus_1
            output_in_iteration_minus_1 = output

            output_list.append(output)

        return output_list
    else:
        return ">>> error: wrong number"





# >>>>>>>>>>>>>>>>>>> MAIN <<<<<<<<<<<<<<<<<<<<<


print("------------------------------------------------")
print("program that returns a Fibonnaci seqence")

try:
    length_of_fibonnaci_sequece = int(input("\nhow many numbers in the sequence you want to generate?: "))
    print("\n>>> your Fibonnaci seqence: {}".format(fibonnaci_sequece_generator(length_of_fibonnaci_sequece)))
except ValueError:
    print("\n>>> this was now a integer number!")