import sys
from collections import deque

sys.stdin = open("inflearn/mysolution/input.txt", "rt")

n = int(input())
apple = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
visited[n//2][n//2] = 1
all_sum = 0
all_sum += apple[n//2][n//2]
que = deque()
que.append((n//2, n//2))
limit = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

print(apple)

while True:
    if limit == n//2:
        break
    size = len(que)
    for i in range(size):
        center = que.popleft()
        for move in range(len(dx)):
            x = center[0] + dx[move]
            y = center[1] + dy[move]
            if visited[x][y] == 0:
                que.append((x, y))
                all_sum += apple[x][y]
                visited[x][y] = 1
    limit += 1
    print(all_sum)
