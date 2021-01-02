'''
    Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
'''

import datetime
now = datetime.datetime.now()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def years_to_100(self):
        print(self.name + " have " + str(100 - self.age) + " years left to 100!")

    def date_when_turn_100(self):

        print(self.name + " will have 100 in: " + str(now.year + 100 - self.age))




while True:
    name = input("give me a person name: ")
    age = input("give me a person age: ")
    person = Person(name, int(age))

    #print(r.name)
    person.years_to_100()
    person.date_when_turn_100()
    print("----------------------")