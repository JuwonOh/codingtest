import sys
sys.stdin = open("inflearn/mysolution/input.txt", "rt")

n = int(input())
c_list = [list(map(int, input().split())) for _ in range(n)]
max_pay = 0


def dfs(index, t_pay):
    global max_pay
    if index == n:
        if max_pay < t_pay:
            max_pay = t_pay

    else:
        if (index + c_list[index][0]) <= n:
            dfs(index + c_list[index][0], t_pay + c_list[index][1])
        dfs(index + 1, t_pay)


dfs(0, 0)
print(max_pay)
