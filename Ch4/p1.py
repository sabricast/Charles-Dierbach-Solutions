# Write a Python program that prompts the user for a list of integers,
# stores in another list only those values between 1–100, and displays the resulting list.

lst = []
terminate = False

while not terminate:
    num = input('Please, enter an integer number (and q to finish): ')

    if num != 'q':
        num = int(num)
        if 1 <= num <= 100:
            lst.append(num)
    else:
        terminate = True
print(lst)
