# Write a Python function named getDailyTemps that prompts the user for the average temperature
# for each day of the week, and returns a dictionary containing the entered information.

def getDailyTemps():
    """
    Returns a dictionary with the average temperature for each day of the week. The average temperature is given
    by the user.

    \>>> getDailyTemps():
        Enter the average temperature for Sunday: 69.0
        Enter the average temperature for Monday: 70.0
        Enter the average temperature for Tuesday: 71.0
        Enter the average temperature for Wednesday: 72.0
        Enter the average temperature for Thursday: 71.5
        Enter the average temperature for Friday: 71.0
        Enter the average temperature for Saturday: 73.0
        -> {'sun': 69.0, 'mon': 70.0, 'tue': 71.0, 'wed': 72.0, 'thu': 71.5, 'fri': 71.0, 'sat': 73.0}

    """

    avg_temperatures = dict()
    avg_temperatures['sun'] = float(input('Enter the average temperature for Sunday: '))
    avg_temperatures['mon'] = float(input('Enter the average temperature for Monday: '))
    avg_temperatures['tue'] = float(input('Enter the average temperature for Tuesday: '))
    avg_temperatures['wed'] = float(input('Enter the average temperature for Wednesday: '))
    avg_temperatures['thu'] = float(input('Enter the average temperature for Thursday: '))
    avg_temperatures['fri'] = float(input('Enter the average temperature for Friday: '))
    avg_temperatures['sat'] = float(input('Enter the average temperature for Saturday: '))

    return avg_temperatures


# --- main

print(getDailyTemps())