from collections import deque
import sys

sys.stdin = open(
    "C:/Users/13a71/OneDrive/문서/OneDrive/github/codingtest/inflearn/섹션 7/15/in5.txt", "rt")

g, s = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(s)]
visited = [[0] * g for _ in range(s)]
que = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


for i in range(s):
    for j in range(g):
        if box[i][j] == 1:
            que.append((i, j))

len_que = len(que)
flag = 0
cnt = 0

while que:
    len_que = len(que)
    for _ in range(len_que):
        current = que.popleft()
        for move in range(4):
            change_x = current[0] + dx[move]
            change_y = current[1] + dy[move]
            if 0 <= change_x < s and 0 <= change_y < g and box[change_x][change_y] == 0:
                box[change_x][change_y] = box[current[0]][current[1]] + 1
                que.append((change_x, change_y))
    cnt += 1
max_val = 0
breaker = False
for i in range(s):
    for j in range(g):
        if box[i][j] == 0:
            print(-1)
            breaker = True
            break
        if max_val < box[i][j]:
            max_val = box[i][j]
    if breaker == True:
        break

else:
    print(cnt, max_val-1)
