# Write a Python program that prompts the user to enter integer values
# for each of two lists. It then should display whether the lists are
# of the same length, whether the elements in each list sum to the same
# value, and whether there are any values that occur in both lists.

lst1 = []
lst2 = []
endlst1 = False
endlst2 = False

# create list 1
while not endlst1:
    entry1 = input('Please, enter a list of numbers and press enter when done: ')
    if entry1 != '':
        entry1 = int(entry1)
        lst1.append(entry1)
    else:
        endlst1 = True

# create list 2
while not endlst2:
    entry2 = input('Please, enter a second list of numbers and press enter when done: ')
    if entry2 != '':
        entry2 = int(entry2)
        lst2.append(entry2)
    else:
        endlst2 = True

# compare the lists
print('Are lists of the same lenght?', len(lst1) == len(lst2))
print('Do both list sum to the same number?', sum(lst1) == sum(lst2))

lst = [x for x in lst1 if x in lst2]

print('The following numbers are repeated in the two lists: ', lst)
