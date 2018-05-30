# Same as p2 but asking for 6 decimals with scientific notation

number1 = float(input('Enter a dividend: '))
number2 = float(input('Enter a divisor: '))

result = number1/number2
print(number1, 'over', number2, 'is', format(result, '.6e'))  # only changed the f for an e
