# N * M크기의 얼음 틀이 있을때, 구멍이 0, 칸막이는 1
# 얼음틀 모양이 주어졌을때 생선되는 총 아이스크림의 갯수를 구하시오.

graph = [[0, 0, 1, 1, 0],
         [0, 0, 0, 1, 1],
         [1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0]]

# BFS/DFS로 해결 가능. 연결 요소의 갯수로 생각 가능. 그래프 형태로 생각. 상하좌우를 인접한 노드로 생각하고 생각.
# 특정 지점에서 BFS, DF,를 진행해서 가능한 모든 노드를 방문해서 방문 처리를 하는게 가능.

# DFS를 활용하는 알고리즘
# 1. 특정한 지점의 주변 상,하,좌,우를 살펴본 뒤에 주변 지점에서 값이 0이면서 아직 방문하지 못한 지점이 있으면, 해당 지점을 방문한다.
# 2. 방문한 지점에서 다시 상,하,좌,우를 살펴보면서 방문을 진행하는 과정을 반복하면, 연결된 모든 지점을 방문할 수 있다.
# 3. 모든 노드에 대해서 1~2의 작업을 반복하여, 방문하지 않은 지점의 수를 카운트 한다.

m = 5
n = 4

# 특정 노드를 방문하고, 연결된 모든 노드를 방문


def dfs(x, y):
    # 주어진 범위를 넘어가면 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
   # 현재 노드를 아직 방문하지 않았으면
    if graph[x][y] == 0:
        # 해당 노드를 방문 처리
        graph[x][y] = 1
        # 상하 좌우의 위치를 전부 호출 가능
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


result = 0

for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result)
