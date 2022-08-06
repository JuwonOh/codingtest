import sys
sys.stdin = open("inflearn/mysolution/input.txt", "rt")

n, m = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n)]
visited = [0] * (n+1)
cnt = 0
res = []

for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1


def DFS(node):
    global cnt
    if node == n:
        cnt += 1
        res.append([i for i, x in enumerate(visited) if x])
    else:
        for i in range(1, n + 1):
            if visited[i] == 0 and graph[node][i] == 1:
                visited[i] = 1
                DFS(i)
                visited[i] = 0


visited[1] = 1
DFS(1)
print(cnt)
print(res)
