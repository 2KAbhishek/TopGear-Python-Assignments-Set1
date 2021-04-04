#!/usr/bin/env python

import sys

a, b, c = sys.argv[1:4]
print(' '.join(sys.argv[1:]))

if a == b == c:
    print('All are same')
else:
    print(max(a, b, c), 'is the biggest')
