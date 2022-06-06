# K번째 수

import sys
sys.stdin = open("input.txt", "rt")
T = int(input())

for t in range(T):
    N, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))[s-1: e]
    a.sort()
    print("#{} {}".format(t, a[k-1]))
