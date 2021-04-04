#!/usr/bin/env python

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))
c = int(input('Enter 3rd number: '))

if a == b == c:
    print('All are same')
else:
    print(max(a, b, c), 'is the biggest')
