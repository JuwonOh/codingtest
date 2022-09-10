from collections import deque
import sys

sys.stdin = open("inflearn/mysolution/input.txt", "rt")

maze = [list(map(int, input().split()))for _ in range(7)]
cnt = 0
maze[0][0] = 1
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    global cnt
    if x == 6 and y == 6:
        cnt += 1

    else:
        for move in range(4):
            x_change = x + dx[move]
            y_change = y + dy[move]
            if 0 <= x_change <= 6 and 0 <= y_change <= 6 and maze[x_change][y_change] == 0:
                maze[x_change][y_change] = 1
                dfs(x_change, y_change)
                maze[x_change][y_change] = 0

dfs(0, 0)
print(cnt)
