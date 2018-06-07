# Write a function called convertStatus that is passed status code 'f', 's', 'j', or 'r' and
# returns the string 'freshman', 'sophomore', 'junior', or 'senior', respectively.
# Design your function so that if an inappropriate letter is passed, an error value
# is returned. Make sure to include an appropriate docstring with your function.


def convertStatus(code):

    """ Returns college standing according to the letter entered.

        Returns a ValueError exception if the letter is not f,s,j, or r.
    """

    if code in ('f', 's', 'j', 'r'):
        if code == 'f':
            return 'freshman'
        elif code == 's':
            return 'sophomore'
        elif code == 'j':
            return 'junior'
        else:
            return 'senior'
    else:
        raise ValueError('Invalid status')

