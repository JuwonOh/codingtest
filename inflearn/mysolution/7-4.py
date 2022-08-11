import sys
sys.stdin = open("inflearn/mysolution/input.txt", "rt")

b = int(input())
tc = int(input())

c_list = [list(map(int, input().split())) for _ in range(tc)]
cnt = 0


def dfs(index, t_sum):
    global cnt
    if t_sum > b:
        return
    if index == tc:
        if t_sum == b:
            cnt += 1
    else:
        for i in range(c_list[index][1] + 1):
            dfs(index + 1, t_sum + c_list[index][0] * i)


dfs(0, 0)
print(cnt)
