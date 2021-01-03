'''
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
'''

def palindrome_of_string_check(string):
    print("inputed string: " + string_from_user + "; string writen backwards: " + string_from_user[::-1])
    if string_from_user == string_from_user[::-1]:
        print("this string is palindrome")
    else:
        print("this string is not palindrome!")


print("program that check string is a palindrome or not")
string_from_user = input("give me a string: ")

palindrome_of_string_check(string_from_user)