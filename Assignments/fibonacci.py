#!/usr/bin/env python
def fib(a, b):
    a, b = b, a+b
    return a, b


n = int(input('Enter number of elements: '))
first, second = 0, 1
lst = []
while len(lst) < n:
    first, second = fib(first, second)
    lst.append(second)
print(lst)


maxNum = int(input('Enter the maximum number: '))
first, second = 1, 1
while(second < maxNum):
    first, second = fib(first, second)
    print(first)
