#!/usr/bin/env python

names = ['Abhishek', 'Abhi', '2K', '2KAbhishek', 'iam']

exist = 'Abhishek'
notExist = 'Random'

print(exist, 'is present: ', exist in names)
print(notExist, 'is present: ', notExist in names)

print(exist, 'is present: ', True if names.index(exist) >= 0 else False)
try:
    print(notExist, 'is present: ', names.index(notExist))
except ValueError:
    print(notExist, 'is not present.')

print('Reversed list: ', names[::-1])
