#!/usr/bin/env python

def opt_backtrack(items, c):
    n = len(items)
    table = [[0 for _ in range(c + 1)] for _ in range(n + 1)]

    # opt
    for i in range(1, n + 1):
        value, weight = items[i - 1]
        for w in range(c + 1):
            if weight <= w:
                table[i][w] = max(table[i - 1][w], table[i - 1][w-weight] + value)
            else:
                table[i][w] = table[i-1][w]

    # backtracking
    chosen_indices = []
    w = c
    for i in range(n, 0, -1):
        if table[i][w] != table[i-1][w]:
            chosen_indices.append(i - 1)
            w -= items[i - 1][1]

    return len(chosen_indices), chosen_indices


def main():
    inp = input()
    while len(inp.strip()) > 0:
        capacity, no_items = inp.split()
        capacity = int(capacity)
        no_items = int(no_items)
        items = []

        for _ in range(no_items):
            items.append(list(map(int, input().split())))

        count, indices = opt_backtrack(items, capacity)

        print(count)

        final_res = []
        for i in indices:
            final_res.append(str(i))
        print(" ".join(final_res))

        #print(table)
        items.clear()
        table = []
        final_res.clear()
        inp = input()

try:
    main()
except EOFError:
    exit(0)