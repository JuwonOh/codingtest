# n *m 공간의 미로가 있을 때, 괴물을 피해서 탈출해야 한다.
# 동빈의 위치는 (1,1)이고, 출구는 (n.m)이며 한번에 한 칸씩 이동할 수 있다.
# 괴물의 위치는 0으로 없는 부분은 1이다.
# 움직여야 하는 최소칸을 구하라.

from collections import deque
n = 5
m = 6
graph = [[1, 0, 1, 0, 1, 0],
         [1, 1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0, 1],
         [1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1]]

# 해결 idea: BFS 사용
# bfs의 특징: 간선의 비용이 전부 같을때 최단거리를 탐색하는 방법
# 가까운 노드부터 모든 모드를 탐색.
# 처음의 위치에서 시작해서 -> 인접한 노드에서 가능한 노드에 1을 더함(거리) -> bfs를 수행하염 최단경로가 1씩 증가하는 방식으로 진행

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시한다.
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시함
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우만 최단거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    # 가장 오른똑 아래까지의 최단 거리 반환
    return graph[n - 1][n - 1]


print(bfs(0, 0))
