import sys
from collections import deque

sys.stdin = open("inflearn/mysolution/input.txt", "rt")

n = int(input())
height = [list(map(int, input().split())) for _ in range(n)]
max_height = max([max(i) for i in height])
cnt = 0
res = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y, h):
    visited[x][y] = 1
    for i in range(4):
        change_x = x + dx[i]
        change_y = y + dy[i]
        if 0 <= change_x < n and 0 <= change_y < n and visited[change_x][change_y] == 0 and height[change_x][change_y] > h:
            dfs(change_x, change_y, h)


for m_height in range(max_height):
    visited = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and height[i][j] > m_height:
                cnt += 1
                dfs(i, j, m_height)
            if cnt > res:
                res = cnt
print(res)
# 비가 내릴때 가장 많은 구획이 남는 경우를 찾는 문제
