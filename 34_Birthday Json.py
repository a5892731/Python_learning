'''
This exercise is Part 2 of 4 of the birthday data exercise series. The other exercises are: Part 1, Part 3, and Part 4.

In the previous exercise we created a dictionary of famous scientists’ birthdays. In this exercise, modify your program
from Part 1 to load the birthday dictionary from a JSON file on disk, rather than having the dictionary defined in
the program.

Bonus: Ask the user for another scientist’s name and birthday to add to the dictionary, and update the JSON file you
have on disk with the scientist’s name. If you run the program multiple times and keep adding new names,
your JSON file should keep getting bigger and bigger.
'''

import json

class Person:
    version = "1.01"
    persons_dict = {}

    def __init__(self):
        self.id = ""
        self.first_name = ""
        self.last_name = ""
        self.age = ""

    def add_person(self):
        self.id = input("give me a person id: ")
        self.first_name = input("give me a person name: ")
        self.last_name = input("give me a person last name: ")
        self.age = input("give me a person age: ")

    def add_person_from_data(self, id, first_name, last_name, age):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def save_to_dict(self, person):
        self.persons_dict[self.id] = person

    def remove_from_dict(self, id):
        try:
            self.persons_dict.pop(id)
        except KeyError:
            print("empty dict")

    def printing(self):
        print("ID: {}".format(self.id))
        print("Name: {}".format(self.first_name))
        print("Last name: {}".format(self.last_name))
        print("Age: {}".format(self.age))

    def printing_dict(self):
        for id in self.persons_dict.keys():
            print("-----------------")
            person.persons_dict[id].printing()
            print("-----------------")

    def save_to_file(self):
        persons_list = []
        for id in self.persons_dict.keys():
            persons_list.append({"ID": self.persons_dict[id].id,
                                 "Name": self.persons_dict[id].first_name,
                                 "Last name": self.persons_dict[id].last_name,
                                 "Age": self.persons_dict[id].age})

        with open("34_Persons.txt", "w") as file:
            json.dump(persons_list, file)
        file.close()

    def read_from_file(self):

        with open('34_Persons.txt') as file:
            data = json.load(file)
            for p in data:
                person = Person()
                person.add_person_from_data(p['ID'], p['Name'], p['Last name'], p['Age'])
                person.save_to_dict(person)

    def clear_file(self):
        open('34_Persons.txt', 'w').close()

    def print_from_file(self):
        with open('34_Persons.txt') as file:
            data = json.load(file)
            for p in data:
                print("-----------------")
                print("ID: {}".format(p["ID"]))
                print("Name: {}".format(p["Name"]))
                print("Last name: {}".format(p["Last name"]))
                print("Age: {}".format(p["Age"]))





# ----------------MAIN------------------
person = Person()

while True:

    print("press 1 for add person")
    print("press 2 for print persons")
    print("press 3 for remove person")
    print("press 4 for print last data")
    print("press 5 for save data to file")
    print("press 6 for read data from file")
    print("press 7 for print data from file")
    print("press 8 for clear file")
    chose = input(">>>> your chose: ")
    print("-----------------")


    if chose == "1":
        person = Person()
        person.add_person()
        person.save_to_dict(person)

    elif chose == "2":
        person.printing_dict()

    elif chose == "3":
        person.remove_from_dict(input("give me a person id: "))

    elif chose == "4":
        person.printing()

    elif chose == "5":
        person.save_to_file()

    elif chose == "6":
        person.read_from_file()

    elif chose == "7":
        person.print_from_file()

    elif chose == "8":
        person.clear_file()
    else:
        print("wrong data")


    print("----------------------")

