import sys
sys.stdin = open("inflearn/mysolution/input.txt", "rt")

n = int(input())
c_list = list(map(int, input().split()))
c_list = sorted(c_list, reverse=True)
res = 1000000000
m = int(input())


def DFS(index, t_sum):
    global res
    if index > res:
        return
    if t_sum > m:
        return
    if t_sum == m:
        if index < res:
            res = index
    else:
        for i in range(n):
            DFS(index + 1, t_sum + c_list[i])


DFS(0, 0)
print(res)
