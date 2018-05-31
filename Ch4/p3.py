# Write a Python program that prompts the user for a list of integers and
# stores them in a list. For all values that are greater than 100, the string
# 'over' should be stored instead. The program should display the resulting list.

lst = []
terminate = False

while not terminate:
    num = input('Please, enter an integer (q to exit): ')
    if num != 'q':
        num = int(num)
        if num <= 100:
            lst.append(num)
        else:
            lst.append('over')
    else:
        terminate = True
print(lst)
