import sys
from collections import deque

sys.stdin = open("inflearn/mysolution/input.txt", "rt")

n = int(input())
isle = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dx = [1, 1, 1, -1, -1, -1, 0, 0]
dy = [0, 1, -1, 0, 1, -1, 1, -1]


def dfs(x, y):
    if 0 <= x < n or 0 <= y < n:
        return False
    if visited[x][y] == 1:
        visited[x][y] = 0
        for move in range(4):
            dfs(x + dx[move])
