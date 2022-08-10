import sys
sys.stdin = open("inflearn/mysolution/input.txt", "rt")

n = int(input())
c_list = list(map(int, input().split()))
last = sum(c_list)
num_list = [i for i in range(1, last+1)]


def dfs(index, t_sum):
    if index == n:
        if t_sum in num_list:
            num_list.remove(t_sum)
    else:
        dfs(index + 1, t_sum + c_list[index])
        dfs(index + 1, t_sum - c_list[index])
        dfs(index + 1, t_sum)


dfs(0, 0)
print(len(num_list))
