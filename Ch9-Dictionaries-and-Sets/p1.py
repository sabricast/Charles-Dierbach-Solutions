# Write a Python function called addDailyTemp that is given a (possibly empty)
# dictionary meant to hold the average daily temperature for each day of the week,
# the day, and the day’s average temperature. The function should add the temperature
# to the dictionary only if does not already contain a temperature for that day.
# The function should return the resulting dictionary, whether or not it is updated.


def addDailyTemp(dictionary, day, temp):

    """ If day is not already in dictionary, adds day and temp to dictionary, using day as the key value.
    (dict, str, float) -> dict

    \>>> addDailyTemp({'sun': 68.8, 'mon' : 70.2}, 'tue', 69.0) -> {'sun': 68.8, 'mon' :70.2,
        'tue': 69.0}
    \>>> addDailyTemp({'sun': 68.8, 'mon' : 70.2}, 'sun', 69.0) -> {'sun': 68.8, 'mon' :70.2}

    """

    if day not in dictionary:
        dictionary[day] = temp
    return dictionary


# -- main, two examples


d = {'sun': 68.8, 'mon': 70.2}

print(addDailyTemp(d, 'sun', 69.0))
print(addDailyTemp(d, 'tue', 69.0))

d2 = {}

print(addDailyTemp(d2, 'sun', 69.0))
print(addDailyTemp(d2, 'tue', 69.0))
