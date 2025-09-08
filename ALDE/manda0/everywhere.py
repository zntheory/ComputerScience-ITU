#!/usr/bin/env python

testcases = int(input())

hs = set()

for t in range(testcases):
    city_number = int(input())
    for c in range(city_number):
        x = input()
        hs.add(x)
    print(len(hs))
    hs.clear()

