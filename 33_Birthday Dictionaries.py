'''
This exercise is Part 1 of 4 of the birthday data exercise series. The other exercises are: Part 2, Part 3, and Part 4.

For this exercise, we will keep track of when our friend’s birthdays are, and be able to find that information based
on their name. Create a dictionary (in your file) of names and birthdays. When you run your program it should ask
the user to enter a name, and return the birthday of that person back to them. The interaction should look something
like this:

#>>> Welcome to the birthday dictionary. We know the birthdays of:
Albert Einstein
Benjamin Franklin
Ada Lovelace
#>>> Who's birthday do you want to look up?
Benjamin Franklin
#>>> Benjamin Franklin's birthday is 01/17/1706.
Happy coding!
'''


def get_persons_list(file_address):
    file = open(file_address, 'r')
    names_and_birthdays_dict = {}

    for line in file:
        person_name = line[0 : len(line.rstrip("\n")) - 11 ]
        person_birthday = line.rstrip("\n")[-10::]
        names_and_birthdays_dict[person_name] = person_birthday

    file.close()
    return names_and_birthdays_dict


#------------------------MAIN------------------------
names_and_birthdays_dict = get_persons_list("33_Birthday Dictionary.txt")

print(">>> Welcome to the birthday dictionary. We know the birthdays of:")
[print(name) for name in names_and_birthdays_dict]
person_choice = input(">>> Who's birthday do you want to look up?\n")
if person_choice in names_and_birthdays_dict:
    print(">>> {}'s birthday is {}".format(person_choice, names_and_birthdays_dict[person_choice]))
else:
    print("Error 404 - person not found")