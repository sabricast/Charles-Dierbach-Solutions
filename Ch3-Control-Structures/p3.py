# Program that displays college standing depending on number of credits

cred = int(input('Please, enter your number of college credits: '))

if cred > 90:
    print('Senior Status')
elif cred > 60:
    print('Junior Status')
elif cred > 30:
    print('Sophomore Status')
else:
    print('Freshman Status')
