# User inputs 2 integer values, program displays result of the
# first divided by the second with exactly 2 decimal places

number1 = int(input('Enter an integer dividend: '))
number2 = int(input('Enter an integer divisor: '))

result = number1/number2
print(number1, 'over', number2, 'is', format(result, '.2f'))

