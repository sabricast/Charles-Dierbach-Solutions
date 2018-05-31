# Same as p6 but using just 1 while loop

current_number = 1
current_column = 1

while current_number < 101:
    if current_column < 11:
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

# Neat version that I found online and wanted to keep for reference

num = 1
while num <= 100:
    print(format(num, '>4d'), end='')
    if num % 10 == 0:
        print()

    num = num + 1
