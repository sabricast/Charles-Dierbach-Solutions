# Write a Python function named checkQuotes that is given a line read from a text file and returns True
# if each quote characters in the line has a matching quote (of the same type), otherwise returns False.


def checkQuotes(line):
    """ Returns True if all quote characters in line are matching. Otherwise it returns False. """

    for x in line:
        if x in ('\'', '"'):
            if line.count('\'') % 2 == 0 and line.count('"') % 2 == 0:
                return True
            else:
                return False


# --- main


input_file = open('filename.txt', 'r')
line = input_file.readline()
checkQuotes(line)

input_file.close()
