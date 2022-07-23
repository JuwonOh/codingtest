import sys
from collections import deque

sys.stdin = open("inflearn/mysolution/input.txt", "rt")

require_ori = input()
n = int(input())

for num in range(n):
    curi = deque(input())
    require = deque(require_ori)
    for i in curi:
        re_cur = require.popleft()
        if i != re_cur:
            require.appendleft(re_cur)
        if len(require) == 0:
            print("#{} Yes".format(num+1))
            break
    else:
        print("#{} No".format(num+1))
