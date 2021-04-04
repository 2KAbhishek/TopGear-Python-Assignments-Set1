#!/usr/bin/env python

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))
op = int(input(
    'Enter' + '\n' + '1 for Addition' + '\n' +
    '2 for Subtraction' + '\n' + '3 for Multiplication' + '\n' + '4 for Division:' + '\n' + '->'))

if(op == 1):
    print(f'{a} + {b} = {a+b}')
elif(op == 2):
    print(f'{a} - {b} = {a-b}')
elif(op == 3):
    print(f'{a} * {b} = {a*b}')
elif(op == 4):
    print(f'{a} / {b} = {a/b}')
else:
    print('Invalid operation')
