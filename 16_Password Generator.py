'''
Write a password generator in Python. Be creative with how you generate passwords
- strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
The passwords should be random, generating a new password every time the user asks for a new password.
Include your run-time code in a main method.

Extra:

Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
'''

from random import randint
import string

def week_passwords_list():  # posible upgreade > take passwords from file
    week_paswords = ["123456", "password", "123456789", "12345678", "12345", "111111", "1234567",
                     "sunshine", "qwerty", "princess", "admin", "welcome"] # 12 weakest passwords from 2018 ;)):
    return week_paswords


def get_user_choice(USER_CHOICE_DICTIONARY):
    # USER_CHOICE_DICTIONARY = {"Wrong data": "0", "Week Password": "1", "Strong Password": "2"}

    user_choice = input(">>> give me your choice: ")

    if user_choice not in USER_CHOICE_DICTIONARY.values():
        user_choice = USER_CHOICE_DICTIONARY["Wrong data"]

    return user_choice

def week_password_generator(week_passwords_list):
    number_of_week_passwords_in_list = len(week_passwords_list)
    return week_passwords_list[randint(0, number_of_week_passwords_in_list)]

def strong_passwodr_generator(password_length, ascii_letters = "", digits = "" , punctuation = "" ):

    password = ""
    list_of_signs = list(ascii_letters + digits + punctuation)
    range_of_signs = len(list_of_signs)

    for password_sign in range(password_length):
        password = password + list_of_signs[randint(0, range_of_signs)]  # add a random sign

    return password


# >>>>>>>>>>>>>>>>>>> MAIN <<<<<<<<<<<<<<<<<<<<<


USER_CHOICE_DICTIONARY = {"Wrong data": "0", "Week Password": "1", "Strong Password": "2"}

while True:

    print("-------------------------------------")
    print("this program is a password generator!")
    print("-------------------------------------")
    print("for week password press (1) <<<<<<<<<")
    print("for strong password press (2) <<<<<<<")
    user_choice = get_user_choice(USER_CHOICE_DICTIONARY)
    print(">>> you chose: {}".format(dict(map(reversed, USER_CHOICE_DICTIONARY.items()))[user_choice])) # value : key from GAME_DICTIONARY

    if user_choice == USER_CHOICE_DICTIONARY["Wrong data"]:
        continue
    elif user_choice == USER_CHOICE_DICTIONARY["Week Password"]:
        print(">>> >>> generated week password: {}".format(week_password_generator(week_passwords_list())))
        break
    elif user_choice == USER_CHOICE_DICTIONARY["Strong Password"]:

        password_length = int(input("give me a password length: "))

        output = strong_passwodr_generator(password_length, string.ascii_letters)
        print(">>> >>> generated strong password with only letters: {}".format(output))

        output = strong_passwodr_generator(password_length, string.ascii_letters, string.digits)
        print(">>> >>> generated strong password with only letters and numbers: {}".format(output))

        output = strong_passwodr_generator(password_length, string.ascii_letters, string.digits, string.punctuation)
        print(">>> >>> generated strong password with all signs: {}".format(output))

        break
    else:
        None
