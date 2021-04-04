#!/usr/bin/env python
lst = [n for n in range(1, 101)]
print(lst)
print('Using for loop: ')
for i in range(len(lst)):
    print(f'{lst[i]:02}  {lst[-(i+1)]:02}')

print('Using while loop: ')
cnt = 1
while(cnt <= 100):
    print(f'{lst[cnt-1]:02}  {lst[-(cnt)]:02}')
    cnt += 1

mystring = 'Hello World'
for i in range(len(mystring)):
    print(mystring[i])
