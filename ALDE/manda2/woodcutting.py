#!/usr/bin/env python

tests = int(input())

for test in range(tests):
    order_time = []
    persons = int(input())

    for person in range(persons):
        _ , *wood_time = list(map(int, input().split()))
        order_time.append(sum(wood_time))

    order_time.sort()

    current_wait_time = 0
    total_wait_time = 0
    for order in order_time:
        current_wait_time += order
        total_wait_time += current_wait_time

    avg_time = total_wait_time / persons
    print(avg_time)
