# Write both a non recursive and recursive function that calculates the Fibonacci number
# for any positive integer, defined as follows,
# fib(0) = 0,
# fib(1) = 1,
# fib(n) = fib(n - 1) + fib(n - 2)

# Recursive


def rfib(number):
    """ (int) -> int
    Return the Fibonacci number for any positive integer.
    """
    if number == 0 or number == 1:
        return number
    else:
        return rfib(number - 1) + rfib(number - 2)

# Non recursive


def fib(number): # Version found in https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/,
                 # but modified to really work.
    """ (int) -> int
    Return the Fibonacci number for any positive integer.
    """
    a = 0
    b = 1

    if number == a:
        return a
    elif number == b:
        return b
    else:
        for k in range(2, number + 1):
            c = a + b
            a = b
            b = c
        return b


print(rfib(2))
print(rfib(3))
print(rfib(4))
print(rfib(5))


print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))