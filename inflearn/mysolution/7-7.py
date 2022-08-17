import sys
from collections import deque

sys.stdin = open("inflearn/mysolution/input.txt", "rt")

max_t = 10000
ch = [0] * (max_t+1)
# 거리와 횟수를 나타내는 list
dis = [0] * (max_t + 1)
n, m = map(int, input().split())
# n이 출발지점
ch[n] = 1
dis[n] = 0
dQ = deque()
dQ.append(n)
while dQ:
    now = dQ.popleft()
    if now == m:
        break
    # for문이 tuple값을 하나씩 탐색한다.
    for next in (now-1, now + 1, now + 5):
        if 0 < next <= max_t:
            if ch[next] == 0:
                dQ.append(next)
                ch[next] = 1
                dis[next] = dis[now] + 1

print(dis[m])
