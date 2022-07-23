import sys
from collections import deque

sys.stdin = open("inflearn/mysolution/input.txt", "rt")

n, k = map(int, input().split())
p_list = deque(_ for _ in range(1, n+1))

while p_list:
    for _ in range(k-1):
        poped_val = p_list.popleft()
        p_list.append(poped_val)
    p_list.popleft()
    print(p_list, poped_val)
    if len(p_list) == 1:
        print(p_list[0])
