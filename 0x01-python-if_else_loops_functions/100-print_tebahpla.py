#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1):
    if i % 2 == 0:
        diff = 0
    else:
        diff = 32
        print('{:c}'.format(i), end='')
