#!/usr/bin/env python
lst = [n for n in range(1, 101)]

print('Using for loop:')
for i in lst[1::2]:
    if i == 50:
        break
    elif i in [10, 20, 30, 40, 50]:
        continue
    else:
        print(i)

print('Using while loop:')
cnt = 2
while(cnt <= 100):
    if lst[cnt-1] == 90:
        break
    elif(lst[cnt-1] in [60, 70, 80, 90]):
        cnt += 2
        continue
    else:
        print(lst[cnt-1])
        cnt += 2
