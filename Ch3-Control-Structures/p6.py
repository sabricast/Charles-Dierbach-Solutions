# Write a program using nested while loops that prints the numbers from 1-100 with that format.

current_number = 1
current_column = 1

while current_number < 101:
    while current_column < 11:
        if current_number == 1:
            print('', current_number, '  ', end='')
        elif current_number < 9:
            print(current_number, '  ', end='')
        elif current_number == 99:
            print(current_number, '', end='')
        else:
            print(current_number, ' ', end='')
        current_number = current_number + 1
        current_column = current_column + 1
    if current_column == 11:
        print()
        current_column = 1
