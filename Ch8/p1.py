# Write a Python function called reduceWhitespace that is given a line read from a
# text file and returns the line with all extra whitespace characters between words removed,
# ‘This line has extra space characters’ ➝ ‘This line has extra space characters’


def reduceWhitespace(input_file, output_file):
    """
       For text file input_file, creates a new version in file output_file
        in which all instances of extra spaces are removed.
    """

    blank_space = ' '

    for line in input_file:
        modified_line = line.replace('    ', blank_space).replace('   ', blank_space).replace('  ', blank_space)

        print(modified_line.strip('\n'))
        output_file.write(modified_line)

# --- main (e.g.)


myfile = open('myfile.txt', 'r')
aloha = open('aloha.txt', 'w')
reduceWhitespace(myfile, aloha)

