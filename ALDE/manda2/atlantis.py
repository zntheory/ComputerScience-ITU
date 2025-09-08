#!/usr/bin/env python

number_of_lines = int(input())

stores = []

for line in range(number_of_lines):
    tmp = input().split()
    stores.append(tuple((int(tmp[0]), int(tmp[1]))))

stores = sorted(stores, key=lambda x: (x[0], x[1]))

count = 0
ts = 0

last_included = (0, 0)
for s in stores:
    if (ts + s[0]) <= s[1]:
        count += 1
        ts += s[0]
        last_included = s
    elif (ts + s[0]) <= last_included[1]:
        count += 1
        ts += s[0]

#print(stores)
#print(len(stores))
print(count)
