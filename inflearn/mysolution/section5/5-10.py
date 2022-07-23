import sys
import heapq as hq

sys.stdin = open("inflearn/mysolution/input.txt", "rt")

a = []

while True:
    n = int(input())
    print(n)
    print(a)
    if n == -1:
        break
    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(hq.heappop(a))
    else:
        hq.heappush(a, n)
