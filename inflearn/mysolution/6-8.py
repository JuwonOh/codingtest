import sys
sys.stdin = open("inflearn/mysolution/input.txt", "rt")

n, m = map(int, input().split())
check = [0] * (n + 1)
res = [0] * m
cnt = 0


def DFS(index):
    global cnt
    if index == m:
        for j in range(m):
            print(res[j], end=' ')
        print()
        cnt += 1

    else:
        for i in range(1, n + 1):
            if check[i] == 0:
                check[i] = 1
                res[index] = i
                DFS(index + 1)
                check[i] = 0


DFS(0)
print(cnt)
