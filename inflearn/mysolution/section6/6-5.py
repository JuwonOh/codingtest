import sys
sys.stdin = open("inflearn/mysolution/input.txt", "rt")

c, n = map(int, input().split())
d_list = [int(input()) for _ in range(n)]
res = 0
total = sum(d_list)


def DFS(index, t_sum, p_sum):
    global res
    if t_sum + (total - p_sum) < res:
        return
    if t_sum > c:
        return
    if index == n:
        if res < t_sum:
            res = t_sum
            print(t_sum, res)
    else:
        DFS(index+1, t_sum + d_list[index], p_sum + d_list[index])
        DFS(index+1, t_sum, p_sum + d_list[index])


DFS(0, 0, 0)
print(res)

# 6-4와 유사한 더 느린 방법


def dfs(index, t_sum):
    global res
    if t_sum > c:
        return
    if n == index:
        if t_sum > res:
            res = t_sum
    else:
        dfs(index + 1, t_sum + d_list[index])
        dfs(index + 1, t_sum)
