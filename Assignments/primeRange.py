#!/usr/bin/env python

from math import sqrt, ceil


def checkPrime(i: int) -> bool:
    for j in range(2, ceil(sqrt(i))):
        if(i % j == 0):
            return False
    else:
        return True


high = int(input('Enter highest number: '))
print('Prime numbers in range:', [x for x in range(1, high) if checkPrime(x)])
