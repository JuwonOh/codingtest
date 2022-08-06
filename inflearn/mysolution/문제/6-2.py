# 깊이 우선 탐색(dfs) vs 너비우선 탐색(bfs)

import sys
sys.stdin = open("inflearn/mysolution/input.txt", "rt")


def DFS(v):
    if v > 7:
        return
    else:
        DFS(v*2)
        DFS(v*2 + 1)
        print(v, end=" ")
