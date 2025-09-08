#!/usr/bin/env python

line = input().strip()

s = []

for x in line:
    if x == '<':
        if len(s) != 0:
            s.pop()
    else:
	    s.append(x)

print("".join(map(str,s)))
