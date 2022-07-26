import sys
sys.stdin = open("inflearn/mysolution/input.txt", "rt")

n, m = map(int, input().split())
res = [0] * m


def dfs(index):
    if index == m:
        for j in range(m):
            print(res[j], end=" ")
        print()
    else:
        for i in range(1, n + 1):
            res[index] = i
            dfs(index + 1)


dfs(1)
