# Write both a non recursive and recursive function that displays the rows of asterisks given below,
#                                     **
#                                    ****
#                                   ******
#                                 **********
#                                ************
#                               **************


# Non recursive

def asterisks():
    print(' ' * 5, '*' * 2)
    print(' ' * 4, '*' * 4)
    print(' ' * 3, '*' * 6)
    print(' ' * 2, '*' * 8)
    print(' ' * 1, '*' * 10)
    print('' * 1, '*' * 12)


asterisks()

# Recursive

def rasterisks(s=5, num=2):
    if s == 0:
        print('*'*num)
    else:
        print(' '*(s-1), '*'*num)
        return rasterisks(s - 1, num + 2)


rasterisks()