#!/usr/bin/env python

from math import sqrt, ceil


def checkPrime(i: int) -> bool:
    if i > 1:
        for j in range(2, ceil(sqrt(i))):
            if(i % j == 0):
                return False
        else:
            return True


num = int(input('Enter a number: '))
print(num, 'is prime?', checkPrime(num))
