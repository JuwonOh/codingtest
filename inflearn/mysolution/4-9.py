import sys
from collections import deque
from tracemalloc import stop
sys.stdin = open("inflearn/mysolution/input.txt", "rt")

n = int(input())
a_list = list(map(int, input().split()))
print(a_list)

res = []
direction = []
recent = 0

for _ in range(n):
    left = a_list[0]
    right = a_list[-1]
    if left > recent and right > recent:
        if left > right:
            res.append(right)
            direction.append("R")
            a_list = a_list[:-1]
        elif left < right:
            res.append(left)
            direction.append("L")
            a_list = a_list[1:]

    elif left > recent:
        res.append(left)
        direction.append("L")
        a_list = a_list[1:]

    elif recent < right:
        res.append(right)
        direction.append("R")
        a_list = a_list[:-1]

    else:
        break

    recent = res[-1]
print(res, direction)

# 강사님 해법

lt = 0
rt = n - 1
last = 0
res = ''
tmp = []
while lt <= rt:
    if a_list[lt] > last:
        tmp.append((a_list[lt], "L"))
    if a_list[rt] > last:
        tmp.append((a_list[rt], "R"))
    tmp.sort()
    if len(tmp) == 0:
        break
    else:
        res = res + tmp[0][1]
        last = tmp[0][0]
        if tmp[0][1] == "L":
            lt += 1
        else:
            rt += 1
