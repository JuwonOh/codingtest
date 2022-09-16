import sys

sys.stdin = open(
    "C:/Users/13a71/OneDrive/문서/OneDrive/github/codingtest/inflearn/섹션 7/16. 사다리타기/in5.txt", "rt")

ladder = [list(map(int, input().split())) for _ in range(10)]
visited = [[0] * 10 for _ in range(10)]
start = next(i for i, num in enumerate(range(10)) if ladder[9][num] == 2)
dc = [+1, -1]


def dfs(r, c):
    visited[r][c] = 1
    if r == 0:
        print(c)
        return c
    else:
        if c + 1 < 10 and ladder[r][c+1] == 1 and visited[r][c+1] == 0:
            dfs(r, c+1)
        elif 0 <= c-1 and ladder[r][c-1] == 1 and visited[r][c-1] == 0:
            dfs(r, c-1)
        else:
            dfs(r-1, c)


dfs(9, start)
