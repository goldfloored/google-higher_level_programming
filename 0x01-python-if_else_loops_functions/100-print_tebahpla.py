#!/usr/bin/python3
j = 2
for i in range(122, 96, -1):
    if j % 2 == 0:
        print("{:c}".format(i), end='')
    else:
        print("{:c}".format(i).upper(), end='')
    j += 1
