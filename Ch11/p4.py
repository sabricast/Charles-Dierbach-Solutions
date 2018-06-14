# Write both a non recursive and recursive function that converts numbers to base 2.

# Non recursive


def base2(num):
    """ (int) -> int

    Return num in base 2.

    """
    converted_num_ls = []

    while num // 2 > 0:
        converted_num_ls.insert(0, num % 2)
        num = num // 2
    converted_num_ls.insert(0, num % 2)

    converted_num = ''
    for num in converted_num_ls:
        converted_num += str(num)

    return int(converted_num)


# Recursive


def rbase2(num):
    """ (int) -> int

    Return num in base 2.

    """

    if num // 2 == 0:
        return num % 2
    else:
        return int(str(rbase2(num // 2)) + str(num % 2))


