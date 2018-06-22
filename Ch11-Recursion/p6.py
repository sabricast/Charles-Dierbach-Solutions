# Write both a non recursive and recursive function that displays the rows of asterisks given below,
#                                ************
#                                 **********
#                                  ********
#                                   ******
#                                    ****
#                                     **


def asterisks():
    print(format('*','*^12'))
    print('', format('*', '*^10'), '')
    print(format('', '1'), format('*', '*^8'), format('', '1'))
    print(format('', '2'), format('*', '*^6'), format('', '2'))
    print(format('', '3'), format('*', '*^4'), format('', '3'))
    print(format('', '4'), format('*', '*^2'), format('', '4'))


asterisks()


def rasterisks(s=0, num=12):
    if s == 5:
        print(' ' * s, '*' * num)
    else:
        print(' ' * s, '*'*num)
        return rasterisks(s + 1, num - 2)


rasterisks()