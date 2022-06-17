# K번째 수

import sys
sys.stdin = open("inflearn/mysolution/input.txt", "rt")
T = int(input())

for _ in range(T):
    n, s, e, k = map(int, input().split())
    a_list = sorted(list(map(int, input().split()))[s-1: e])
    print(a_list[k-1])
