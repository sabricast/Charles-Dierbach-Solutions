# Program that sums a series of positive integers entered by the user,
# excluding all numbers greater than 100.

terminate = False
sum = 0

while not terminate:
    num = int(input('Please, enter an integer: '))
    if num > 0:
        sum = sum + num
    if num == -1:
        terminate = True
print(sum)
