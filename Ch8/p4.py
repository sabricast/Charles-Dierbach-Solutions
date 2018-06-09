# Write a Python function named countAllLetters that is given a line read from a text file and
# returns a list containing every letter in the line and the number of times that each letter
# appears (with upper/lower case letters counted together)


def countAllLetters(line):
    """ Returns a list containing every letter in line and the number of times each letter appears. """

    lst = []
    letters = []
    new_line = line.lower()

    for k in new_line:
        if k not in letters and k != ' ':
            count = new_line.count(k)
            value = (k, count)
            lst.append(value)
            letters.append(k)

    print(lst)
    return lst

# --- main


input_file = open('filename.txt', 'r')
line = input_file.readline()

countAllLetters(line)
input_file.close()


