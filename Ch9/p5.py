# Write a Python function named addVegetable that is passed a (possible empty) set of vegetable names,
# and raises a ValueError exception if the given vegetable is already in the set, otherwise, the new
# vegetable should be added and the new set returned.

def addVegetable(A, veggie):
    """
    Add the veggie to the set A, or raises a ValueError exception if veggie already in A.

    (set) -> set

    \>>> addVegetable({'spinach', 'zucchini', 'broccoli'}, 'spinach') -> ValueError 'Vegetable already in set'
    \>>> addVegetable({'spinach', 'zucchini', 'broccoli'}, 'arugula') -> {spinach, zucchini, broccoli, arugula}

    """

    try:
        if veggie in A:
            raise ValueError('Vegetable already in set')
        A.add(veggie)
        return A
    except ValueError as err_mesg:
        print(err_mesg, '\n')


# --- main


print(addVegetable({'spinach', 'zucchini', 'broccoli'}, 'arugula'))
addVegetable({'spinach', 'zucchini', 'broccoli'}, 'spinach') # printing this commands only returns None because
                                                             # there is no return value associated to it.


