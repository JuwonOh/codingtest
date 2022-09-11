import sys

sys.stdin = open("inflearn/mysolution/input.txt", "rt")

n = int(input())
climb = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cnt = 0


def dfs(x, y):
    global cnt
    if climb[x][y] == max_value:
        cnt += 1
    else:
        for move in range(4):
            x_change = x + dx[move]
            y_change = y + dy[move]
            if 0 <= x_change < n and 0 <= y_change < n and climb[x_change][y_change] > climb[x][y]:
                dfs(x_change, y_change)


def search_min(matrix):
    min_val = float("inf")
    max_val = float("-inf")
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] < min_val:
                min_val = matrix[i][j]
                min_x, min_y = i, j
            if matrix[i][j] > max_val:
                max_val = matrix[i][j]

    return min_x, min_y, max_val


x, y, max_value = search_min(climb)
dfs(x, y)
print(cnt)
