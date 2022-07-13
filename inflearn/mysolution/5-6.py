import sys
from collections import deque

sys.stdin = open("inflearn/mysolution/input.txt", "rt")
n, m = list(map(int, input().split()))
l_list = deque((c, l) for l, c in enumerate(map(int, input().split())))

cnt = 0
while l_list:
    cur = l_list.popleft()
    if any(cur[0] < x[0] for x in l_list):
        l_list.append(cur)
    else:
        cnt += 1
        if cur[1] == m:
            print(cnt)
            break
