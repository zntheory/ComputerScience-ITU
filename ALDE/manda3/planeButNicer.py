#!/usr/bin/env python
import math

original_pl = [] # floats

def dist(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def closest_pair(_list):
    delta = float("inf") # delta = float("inf") # known shortest dist
    delta_pair = [[0.0, 0.0], [0.0, 0.0]]

    if len(_list) > 3:
        middle_index = int((len(_list) / 2)) # cast to int rounds x.5 down to x
        cutoff = _list[middle_index][0]
        left_list = _list[:middle_index] # index 0 to middle_index-1
        right_list = _list[middle_index:] # middle point is here
        left_delta, left_pair = closest_pair(left_list)
        right_delta, right_pair = closest_pair(right_list)
        if left_delta < right_delta:
            delta = left_delta
            delta_pair = left_pair
        else:
            delta = right_delta
            delta_pair = right_pair

        delta_range_list = []
        min_x = cutoff - delta
        max_x = cutoff + delta

        for p in original_pl:
            if min_x < p[0] < max_x: delta_range_list.append(p)
        delta_range_list.sort(key=lambda _p: (_p[1]))

        for i in range(len(delta_range_list)):
            p1 = delta_range_list[i]
            for j in range(min(11, len(delta_range_list)-i-1)): # Min exp calculated each check?
                p2 = delta_range_list[i+j+1]
                current_dist = dist(p1, p2)
                if current_dist < delta:
                    delta = current_dist
                    delta_pair[0] = p1
                    delta_pair[1] = p2
    else:
        for i in range(len(_list)):
            for j in range(len(_list)):
                if i != j:
                    p1 = _list[i]
                    p2 = _list[j]
                    current_dist = dist(p1, p2)
                    if current_dist < delta:
                        delta = current_dist
                        delta_pair[0] = p1
                        delta_pair[1] = p2
    return delta, delta_pair


def main():
    number_of_points = int(input())

    for i in range(number_of_points):
        original_pl.append(list(map(float, input().split())))

    original_pl.sort(key=lambda _p: (_p[0]))
    final_delta, final_pair = closest_pair(original_pl)
    #print(final_delta)
    #print(final_pair)

    print("{0} {1}".format(final_pair[0][0], final_pair[0][1]))
    print("{0} {1}".format(final_pair[1][0], final_pair[1][1]))

main()
