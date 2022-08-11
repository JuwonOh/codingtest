import sys
sys.stdin = open("inflearn/mysolution/input.txt", "rt")

n, m = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n)]
visited = [0] * (n+1)
cnt = 0
path = []
print(visited)

for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1

cnt = 0


def dfs(node):
    global cnt
    global path

    if node == n:
        cnt += 1
        path.append([index for index, x in enumerate(visited) if x])
    else:
        for i in range(1, n+1):
            if visited[i] == 0 and graph[node][i] == 1:
                visited[i] = 1
                dfs(i)
                visited[i] = 0


visited[1] = 1
dfs(1)
print(path)
