# User enters 'A', 'B', or 'C' and program displays 'Apple', 'Banana', and 'Coconut', respectively.
# Using nested if statements

terminate = False

while not terminate:
    letter = input('Choose your fruit! Enter A, B, or C (-1 to finish): ')
    if letter == 'A':
        print('Apple!')
    else:
        if letter == 'B':
            print('Banana!')
        else:
            if letter == 'C':
                print('Coconut!')
            else:
                if letter == '-1':
                    print('Thanks for playing!')
                    terminate = True
                else:
                    print('Invalid input! Please try again.')
