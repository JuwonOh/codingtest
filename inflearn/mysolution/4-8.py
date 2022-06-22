import sys
from collections import deque
sys.stdin = open("inflearn/mysolution/input.txt", "rt")

n, m = map(int, input().split())
w_list = list(map(int, input().split()))
w_list.sort()

# que로도 하는 방법이 있다.
que = deque(w_list)

cnt = 0
while w_list:

    w = m
    w -= w_list[-1]
    w_list.pop()
    cnt += 1

    if len(w_list) == 0:
        break

    if w - w_list[0] > 0:
        w_list = w_list[1:]
        # w_list.pop(0)도 가능하다.
print(cnt)

# que로도 하는 방법이 있다.
cnt2 = 0
while que:
    if len(que) == 0:
        break
    cnt2 += 1
    if que[0] + que[-1] < m:
        que.pop()
        que.popleft()
    else:
        que.pop()
    print(cnt2)
