import sys
from collections import deque

sys.stdin = open("inflearn/mysolution/input.txt", "rt")

n = int(input())
apple = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

all_sum = 0
que = deque()
visited[n//2][n//2] = 1
que.append((n//2, n//2))
limit = 0
all_sum += apple[n//2][n//2]

while True:
    if limit == n // 2:
        break
    size = len(que)
    for i in range(size):
        center = que.popleft()
        for move in range(4):
            x = center[0] + dx[move]
            y = center[1] + dy[move]
            if visited[x][y] == 0:
                visited[x][y] = 1
                que.append((x, y))
                all_sum += apple[x][y]
    limit += 1

print(all_sum)
