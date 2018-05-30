# Enter 2 integer values and perform the following operations

integer1 = int(input('Enter the first integer: '))
integer2 = int(input('Enter the second integer: '))

print(integer1, '+', integer2, '=', str(integer1+integer2))
print(integer1, '-', integer2, '=', str(integer1-integer2))
print(integer1, '*', integer2, '=', str(integer1*integer2))
print(integer1, '/', integer2, '=', format(integer1/integer2, ',.2f'))
print(integer1, '//', integer2, '=', str(integer1//integer2))
print(integer1, '%', integer2, '=', str(integer1 % integer2))
print(integer1, '**', integer2, '=', format(integer1**integer2, ',.2f'))
