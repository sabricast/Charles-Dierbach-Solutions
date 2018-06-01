# Write a Python program that prompts the user to enter a list of words and stores
# in a list only those words whose first letter occurs again within the word
# (for example, 'Baboon'). The program should display the resulting list.

lst = []
terminate = False
empty_str = ''

# getting input from user
while not terminate:
    entry = input('Please, enter a list of words (and press enter when done): ')
    if entry != empty_str:
        lst.append(entry)
    else:
        terminate = True

# returning only words with the first letter re-occurring
output = []
for k in range(len(lst)):
    lcase = (lst[k][0]).lower()
    if lcase in lst[k]:
        output.append(lst[k])

print(output)


