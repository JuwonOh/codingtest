import sys
sys.stdin = open("inflearn/mysolution/input.txt", "rt")

n, f = map(int, input().split())
check = [0] * (n+1)
res = [0] * n
b = [1] * n
for i in range(1, n):
    b[i] = b[i-1] * (n - i) // i


def DFS(index, t_sum):
    if t_sum == f and index == n:
        for j in range(n):
            print(res[j], end=' ')
        print()

    else:
        for i in range(1, n + 1):
            if check[i] == 0:
                check[i] = 1
                res[index] = i
                DFS(index + 1, t_sum + (res[index] * b[index]))
                check[i] = 0


DFS(0, 0)
