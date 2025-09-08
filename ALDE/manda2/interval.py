#!/usr/bin/env python

number_of_lines = int(input())

list = []

for line in range(number_of_lines):
    tmp = input().split()
    list.append(tuple((int(tmp[0]), int(tmp[1]))))

def func(e):
    return e[1]

list.sort(key=func)

#print(list)

count = 0
current_time = 0

for t in list:
    if current_time <= t[0]:
        count += 1
        current_time = t[1]

print(count)
