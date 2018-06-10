# Write a Python function named moderateDays that is given a dictionary containing
# the average daily temperature for each day of a week, and returns a list of the days
# in which the average temperature was between 70 and 79 degrees.

def moderateDays(dictionary):
    """
    Returns a list with the key values of dictionary which associated values were between 70 and 79.

    dictionary -> list

    \>>> moderateDays({'mon': 69.9, 'tue': 89.0, 'wed': 65.4, 'thu': 67.9, 'fri': 70.6, 'sat': 71.0,
         'sun': 76.7}) -> ['fri', 'sat', 'sun']
    """
    lst = []

    for k in dictionary:
        if dictionary[k] >= 70 and dictionary[k] <= 79:
            lst.append(k)
    return lst

# -- main


print(moderateDays({'mon': 69.9, 'tue': 89.0, 'wed': 65.4, 'thu': 67.9, 'fri': 70.6, 'sat': 71.0, 'sun': 76.7}))
print(moderateDays({'mon': 70.3, 'tue': 89.0, 'wed': 75.0, 'thu': 67.9, 'fri': 70.6, 'sat': 71.0, 'sun': 76.7}))

