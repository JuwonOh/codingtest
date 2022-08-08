import sys
sys.stdin = open("inflearn/mysolution/input.txt", "rt")

n, m = map(int, input().split())
res = [0] * (map + 1)


def DFS(index, sequence):
    global temp
    if index == m:
        for j in range(m):
            print(res[j], end=" ")
        print()
    else:
        for i in range(sequence, n + 1):
            res[index] = i
            DFS(index + 1, i + 1)


DFS(0, 1)
