#!/usr/bin/env python
str1 = input('Enter a string: ')
print(' '.join(str1))
print('Sliced string:', str1[len(str1)/2 - len(str1) - 1])
print('Repeating string: ', str1 * 100)
str2 = input('Enter another string: ')
print('After concatenation', str1 + str2)
