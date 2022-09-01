import sys
from collections import deque

sys.stdin = open("inflearn/mysolution/input.txt", "rt")

max_t = 10000
check = [0] * (max_t + 1)
distance = [0] * (max_t + 1)
n, m = map(int, input().split())
check[n] = 1
distance[n] = 0
dQ = deque()
dQ.append(n)

while dQ:
    now = dQ.popleft()
    if now == m:
        break
    for next_step in (now - 1, now + 1, now + 5):
        if 0 < next_step < max_t:
            if check[next_step] == 0:  # 방문을 안했을 때만
                dQ.append(next_step)
                check[next_step] = 1
                distance[next_step] = distance[now] + 1
print(distance[m])
