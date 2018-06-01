# Write a Python program that prompts the user to enter a list of
# first names and stores them in a list. The program should display
# how many times the letter 'a' appears within the list.

lst = []
terminate = False

while not terminate:
    entry = input('Please enter a first name (and q to exit): ')
    if entry != 'q':
        lst.append(entry)
    else:
        terminate = True

num_of_a = 0

for k in range(len(lst)):
    num = [x for x in lst[k] if x == 'a']
    num_of_a = num_of_a + len(num)
print("The number of  a's in your list is", num_of_a)



