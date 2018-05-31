# Write a Python program that prompts the user for a list of integers,
# stores in another list only those values that are in tuple valid_values,
# and displays the resulting list.

lst = []
terminate = False
valid_values = (1, 3, 5, 7, 10, 15, 70, 34)

while not terminate:
    num = input('Please, enter an integer number (and q to finish): ')

    if num != 'q':
        num = int(num)
        if num in valid_values:
            lst.append(num)
    else:
        terminate = True
print(lst)
