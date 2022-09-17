from collections import deque


def bfs(x, y, maps):
    n = len(maps)  # 세로
    m = len(maps[0])  # 가로
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[x][y] = True
    queue = deque((x, y))
    while queue:
        if maps[x][y] == 1:
            current = queue.popleft()


def solution(maps):
    answer = bfs(0, 0, maps)
    return answer
