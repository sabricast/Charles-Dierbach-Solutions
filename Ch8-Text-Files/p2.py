# Write a Python function named extractTemp that is given a line read from a text file and displays the
# one number (integer) found in the string,

def extractTemp(line):

    """ Returns the number found in line. """

    for char in line:
        if char in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
            print(char, end='')

# --- main


input_file = open('p2.txt', 'r')
line = input_file.readline()

extractTemp(line)

input_file.close()
