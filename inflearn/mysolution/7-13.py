import sys
from collections import deque

sys.stdin = open("inflearn/mysolution/input.txt", "rt")

n = int(input())
isle = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dx = [1, 1, 1, -1, -1, -1, 0, 0]
dy = [0, 1, -1, 0, 1, -1, 1, -1]

# bfs 코드


sys.stdin = open("inflearn/mysolution/input.txt", "rt")

n = int(input())
isle = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
print(isle)
cnt = 0
queue = deque()
dx = [1, 1, 1, -1, -1, -1, 0, 0]
dy = [0, 1, -1, 0, 1, -1, 1, - 1]

for i in range(n):
    for j in range(n):
        # bfs 에서는 항상 que를 만들고, 넣는게 먼저다.
        if isle[i][j] == 1:
            isle[i][j] = 0
            queue.append((i, j))
            while queue:
                print(queue)
                current = queue.popleft()
                for move in range(8):
                    x = current[0] + dx[move]
                    y = current[1] + dy[move]
                    if 0 <= x < n and 0 <= y < n and isle[x][y] == 1:
                        isle[x][y] = 0
                        queue.append((x, y))
            cnt += 1
print(cnt)

# dfs 시도


def dfs(x, y):
    if 0 <= x < n or 0 <= y < n:
        return False
    if visited[x][y] == 1:
        visited[x][y] = 0
        for move in range(8):
            dfs(x + dx[move])
        else:
            True
    return False


cnt = 0
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            cnt += 1
print(cnt)
