# Write a Python function named interleaveChars that is given two lines read from
# a text file, and returns a single string containing the characters of each string
# interleaved.


def interleaveChars(line1, line2):

    """ Returns a single string containing the characters of line1 and line2 interleaved. """

    new_line = ''
    for k in range(max(len(line1), len(line2))):
        try:
            new_line = new_line + line1[k] + line2[k]
        except IndexError:
            minimum_index = min(len(line1), len(line2))
            if len(line1) < len(line2):
                new_line = new_line + line2[minimum_index:]
                break
            else:
                new_line = new_line + line1[minimum_index:]
                break

    return new_line

# --- main

input_file = open('myfile.txt', 'r')
line1 = input_file.readline().strip('\n')
line2 = input_file.readline().strip('\n')

print(interleaveChars(line1, line2))