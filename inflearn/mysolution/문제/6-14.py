import sys
sys.stdin = open("inflearn/mysolution/input.txt", "rt")

n, m = map(int, input().split())
# 목표 인접행렬을 만드는 것.
graph = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    x, y, val = map(int, input().split())
    graph[x][y] = val

for i in range(1, n+1):
    for j in range(1, n+1):
        print(graph[i][j], end=' ')
    print()
