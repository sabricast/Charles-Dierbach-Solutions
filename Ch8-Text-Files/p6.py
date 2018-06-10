# Write a program segment that opens and reads a text file and displays how many lines of
# text are in the file.

file_name = input('Enter file name (with the extension): ')
count = len(open(file_name).readlines())
print('There are', count, 'lines of text in the file.')
