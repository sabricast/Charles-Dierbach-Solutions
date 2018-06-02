# Write a Python function named modCount that is given a positive integer, n,
# and a second positive integer, m <= n, and returns how many numbers
# between 1 and n are evenly divisible by m.

def modCount(n, m):
    sum = 0
    for k in range(1, n + 1):
       if k % m == 0:
           sum = sum + 1
    return sum