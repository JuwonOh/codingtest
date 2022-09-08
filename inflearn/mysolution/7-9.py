import sys
from collections import deque

sys.stdin = open("inflearn/mysolution/input.txt", "rt")

maze = [list(map(int, input().split())) for _ in range(7)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
que = deque()
que.append((0, 0))
visited = [[0] * 7 for _ in range(7)]
visited[0][0] = 1
x, y = 0, 0
cnt = 0

while que:
    current = que.popleft()
    for move in range(4):
        x = current[0] + dx[move]
        y = current[1] + dy[move]
        if 0 <= x < 7 and 0 <= y < 7:
            if visited[x][y] == 0 and maze[x][y] == 0:
                visited[x][y] = 1
                maze[x][y] = maze[current[0]][current[1]] + 1
                que.append((x, y))
                print(visited)
if visited[6][6] == 0:
    print(-1)
else:
    print(maze[6][6])
