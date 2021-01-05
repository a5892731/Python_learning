'''
Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file,
and print out the results to the screen. I have a .txt file for you, if you want to use it!

Extra:

Instead of using the .txt file from above
(or instead of, if you want the challenge), take this .txt file, and count how many of each “category”
of each image there are. This text file is actually a list of files corresponding to the SUN database
scene recognition database, and lists the file directory hierarchy for the images. Once you take
a look at the first line or two of the file, it will be clear which part represents the scene category.
To do this, you’re going to have to remember a bit about string parsing in Python 3.
I talked a little bit about it in this post.
'''


def get_names_from_file(gender = "Male"):

    def choose_gender_of_name(file_bufor, gender):

        GENDER_DICTIONARY = {"Rank": 0, "Male": 1, "Female": 2}

        names_bufor = []
        for line in range(1, len(file_bufor)):
            names_bufor.append(file_bufor[line][GENDER_DICTIONARY[gender]])
        return names_bufor

    file = open('22_Read From File.txt', 'r', encoding="utf-8") # most popular names ranking in file
    file_bufor = []

    for line in file:
        file_bufor.append(line.split())

    file.close()

    return choose_gender_of_name(file_bufor, gender)




# >>>>>>>>>>>>>>>>>>> MAIN <<<<<<<<<<<<<<<<<<<<<

print("--------------------------------------------")
print("this program gets a list of names from file!")


print(get_names_from_file("Male"))
print(get_names_from_file("Female"))