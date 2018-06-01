# Write a Python program that prompts the user to enter types of fruit,
# and how many pounds of fruit there are for each type. The program should
# then display the information in the form fruit, weight listed in alphabetical
#  order, one fruit type per line,

lst = []
terminate = False

while not terminate:
    fruit = input("""Please enter a fruit and how much pounds of that fruit there is.
Separate the two with a comma (e.g., Banana, 45) (q to finish): """)
    if fruit != 'q':
        lst.append(fruit.split(', '))
        lst.sort()
    else:
        terminate = True

for k in range(len(lst)):
    print(lst[k][0] + ',', lst[k][1], 'lbs.')
