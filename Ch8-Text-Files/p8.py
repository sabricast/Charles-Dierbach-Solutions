# Write a program segment that reads a text file named original_text,
# and displays how many times the letter ‘e’ occurs.

with open('myfile.txt') as original_text:
    num_of_e = 0
    for line in original_text:
        num_of_e += line.count('e')
    print(num_of_e)
