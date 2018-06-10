# Write a Python function named getWeekendAvgTemp that is passed a dictionary of daily temperatures,
# and returns the average temperature over the weekend for the weekly temperatures given.


def getWeekendAvgTemp(dictionary):
    """
    Given a dictionary of daily temperatures, returns a string with the average temperature over the weekend.

    (dictionary) -> str

    \>>> getWeekendAvgTemp({'mon': 69.9, 'tue': 89.0, 'wed': 65.4, 'thu': 67.9, 'fri': 70.6, 'sat': 71.0,
         'sun': 76.7} -> The average temperature over the weekend was 73.9

    """

    avg_weekend = (dictionary['sat'] + dictionary['sun'])/2
    return 'The average temperature over the weekend was ' + str(format(avg_weekend, '.1f'))


# --- main

print(getWeekendAvgTemp({'mon': 69.9, 'tue': 89.0, 'wed': 65.4, 'thu': 67.9, 'fri': 70.6, 'sat': 71.0, 'sun': 76.7}))