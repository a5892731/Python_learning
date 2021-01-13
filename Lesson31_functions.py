



def draw_hangman(error_count):

    def zero_errors():
        print(
        "       ||||||||||||||| "  + "\n" +
        "       |||  ||         "  + "\n" +
        "       |||||           "  + "\n" +
        "       |||             "  + "\n" +
        "       |||             "  + "\n" +
        "       |||             "  + "\n" +
        "|||||||||||||||||      " )

    def one_error():
        print(
        "       ||||||||||||||| "  + "\n" +
        "       |||  ||      |  "  + "\n" +
        "       |||||           "  + "\n" +
        "       |||             "  + "\n" +
        "       |||             "  + "\n" +
        "       |||             "  + "\n" +
        "|||||||||||||||||      " )

    def two_errors():
        print(
        "       ||||||||||||||| "  + "\n" +
        "       |||  ||      |  "  + "\n" +
        "       |||||      ('_')"  + "\n" +
        "       |||             "  + "\n" +
        "       |||             "  + "\n" +
        "       |||             "  + "\n" +
        "|||||||||||||||||      " )

    def three_errors():
        print(
        "       ||||||||||||||| "  + "\n" +
        "       |||  ||      |  "  + "\n" +
        "       |||||      ('_')"  + "\n" +
        "       |||        \ | /"  + "\n" +
        "       |||             "  + "\n" +
        "       |||             "  + "\n" +
        "|||||||||||||||||      " )

    def four_errors():
        print(
        "       ||||||||||||||| "  + "\n" +
        "       |||  ||      |  "  + "\n" +
        "       |||||      ('_')"  + "\n" +
        "       |||        \ | /"  + "\n" +
        "       |||         ( ) "  + "\n" +
        "       |||             "  + "\n" +
        "|||||||||||||||||      " )

    def five_errors():
        print(
        "       ||||||||||||||| "  + "\n" +
        "       |||  ||      |  "  + "\n" +
        "       |||||      ('_')"  + "\n" +
        "       |||        \ | /"  + "\n" +
        "       |||         ( ) "  + "\n" +
        "       |||         /   "  + "\n" +
        "|||||||||||||||||      " )

    def six_errors():
        print(
        "       ||||||||||||||| "  + "\n" +
        "       |||  ||      |  "  + "\n" +
        "       |||||      ('_')"  + "\n" +
        "       |||        \ | /"  + "\n" +
        "       |||         ( ) "  + "\n" +
        "       |||         / \ "  + "\n" +
        "|||||||||||||||||      " )

    print("") # \n

    if error_count == 0:
        zero_errors()
    elif error_count == 1:
        one_error()
    elif error_count == 2:
        two_errors()
    elif error_count == 3:
        three_errors()
    elif error_count == 4:
        four_errors()
    elif error_count == 5:
        five_errors()
    elif error_count == 6:
        six_errors()
    else:
        six_errors()