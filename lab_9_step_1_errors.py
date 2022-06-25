integer = 50
string = "The number is"

try:
    print(string + integer)
except TypeError as err:
    logging.warning("Error - {}. You cannot add a string to an integer, without converting the integer to a string first".format(err))