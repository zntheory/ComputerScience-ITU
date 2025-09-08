#!/usr/bin/env python

import string

N, t = input().split()
A = list(map(int,input().split()))

#if int(N) != len(A):
#    print("taber")
#    print(len(A))

match int(t):
    case 1:
        print(7)
    case 2:
        if A[0] > A[1]:
            print("Bigger")
        elif A[0] == A[1]:
            print("Equal")
        else:
            print("Smaller")
    case 3:
        new_list = [A[0], A[1], A[2]]
        new_list.sort()
        print(new_list[1])
    case 4:
        print(sum(A))
    case 5:
        answer = 0
        for i in A:
            if i % 2 == 0:
                answer += i
        print(answer)
    case 6:
        ascii = string.ascii_letters
        answer = ""
        for i in A:
            answer += ascii[i%26]
        print(answer)
    case 7:
        i = 0
        i == A[i]
        hs = set()
        while True:
            if i in hs:
                print("Cyclic")
                break
            else:
                hs.add(i)
            if i > int(N) or i < 0:
                print("Out")
                break
            if i == int(N) - 1:
                print("Done")
                break
            i == A[i]
