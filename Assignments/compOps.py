#!/usr/bin/env python
nums = list(map(int, input('Enter space seperated numbers(10): ').split(' ')))

avg = sum(nums)/len(nums)

print('More than average:', list(filter(lambda x: x > avg, nums)))
print('Less than average:', list(filter(lambda x: x < avg, nums)))
print('Equal to average:', list(filter(lambda x: x == avg, nums)))
