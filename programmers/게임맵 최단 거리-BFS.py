from collections import deque


def bfs(x, y, maps):
    n = len(maps)  # 세로
    m = len(maps[0])  # 가로
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited = [[False for _ in range(m)] for _ in range(n)]
    queue = deque((x, y))
    while queue:
        if maps[x][y] == 1:
            current = queue.popleft()
            visited[current[0]][current[1]] = True
            for move in range(4):
                change_x = current[0] + dx[move]
                change_y = current[1] + dy[move]
                if 0 <= change_x < n and 0 <= change_y < m and maps[change_x][change_y] == 1 and not visited[change_x][change_y]:
                    visited[change_x][change_y] = True
                    maps[change_x][change_y] = maps[current[0]][current[1]] + 1
                    queue.append((change_x, change_y))
                    if change_x == n-1 and change_y == m-1:
                        return maps[change_x][change_y]


def solution(maps):
    answer = bfs(0, 0, maps)
    return answer
