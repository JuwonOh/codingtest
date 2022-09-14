import sys
from collections import deque

sys.stdin = open("inflearn/mysolution/input.txt", "rt")
n = int(input())
height = [list(map(int, input().split())) for _ in range(n)]
res = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y, h):
    visited[x][y] = 1
    for move in range(4):
        x_change = x + dx[move]
        y_change = y + dy[move]
        if 0 <= x_change < n and 0 <= y_change < n and visited[x_change][y_change] == 0 and height[x_change][y_change] > h:
            dfs(x_change, y_change, h)


max_ht = max(max(i) for i in height)
for water in range(max_ht):
    cnt = 0
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and height[i][j] > water:
                visited[i][j] = 1
                dfs(i, j, water)
                cnt += 1
    if cnt > res:
        res = cnt

print(res)
