# Same as p1 but with floating-point values and six decimals

number1 = float(input('Enter a dividend: '))
number2 = float(input('Enter a divisor: '))

result = number1/number2
print(number1, 'over', number2, 'is', format(result, '.6f'))
