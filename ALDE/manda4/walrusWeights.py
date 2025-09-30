#!/usr/bin/env python

no_plates = int(input())

plates = []
for _ in range(no_plates):
    plates.append(int(input()))

max_weight = 2000
table = [[False for _ in range(max_weight + 1)] for _ in range(no_plates + 1)]

for i in range(no_plates + 1):
    table[i][0] = True

for i in range(1, no_plates + 1):
    plate_weight = plates[i - 1]

    for w in range(0, max_weight + 1):
        take = False
        if plate_weight <= w:
            take = table[i - 1][w - plate_weight]

        table[i][w] = table[i-1][w] | take

intended_weight = 1000

if table[no_plates][intended_weight]:
    print(intended_weight)
    exit(0)

for i in range(intended_weight + 1):
    if table[no_plates][intended_weight + i]:
        print(intended_weight + i)
        exit(0)
    if table[no_plates][intended_weight - i]:
        print(intended_weight - i)
        exit(0)
