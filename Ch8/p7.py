# Write a program segment that reads a text file named original_text, and writes every other line,
# starting with the first line, to a new file named half_text.


half_text = open('half_text.txt', 'w')

with open('filename.txt') as original_text:
    i = 1
    for line in original_text:
        if i % 2 != 0:
            half_text.write(line)
        i += 1

half_text.close()
