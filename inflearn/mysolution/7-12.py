from collections import deque
import sys

sys.stdin = open(
    "C:/Users/13a71/OneDrive/문서/OneDrive/github/codingtest/inflearn/섹션 7/12. 단지번호붙이기/in4.txt", "rt")
n = int(input())
app = [list(map(int, list(input()))) for _ in range(n)]

app_size = []
res = 0
que = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    for j in range(n):
        if app[i][j] == 1:
            each_size = 0
            que.append((i, j))
            app[i][j] = 0
            while que:
                current = que.popleft()
                each_size += 1
                for move in range(4):
                    change_x = current[0] + dx[move]
                    change_y = current[1] + dy[move]
                    if 0 <= change_x < n and 0 <= change_y < n and app[change_x][change_y] == 1:
                        que.append((change_x, change_y))
                        app[change_x][change_y] = 0
            res += 1
            app_size.append(each_size)
print(res)
for i in sorted(app_size):
    print(i)
