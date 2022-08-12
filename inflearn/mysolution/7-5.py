import sys
sys.stdin = open("inflearn/mysolution/input.txt", "rt")

n = int(input())
c_list = [int(input()) for _ in range(n)]
min_differ = sum(c_list)
money = [0] * 3
res = sum(c_list)


def dfs(index):
    global res
    if index == n:
        if len(set(money)) != 3:
            return
        differ = max(money) - min(money)
        if res > differ:
            res = differ
    else:
        for i in range(3):
            money[i] += c_list[index]
            dfs(index + 1)
            money[i] -= c_list[index]


dfs(0)
print(res)


def dfs(index, a, b, c):
    global min_differ
    if index == n:
        if a == b or b == c or c == a:
            return
        min_people = min(a, b, c)
        max_people = max(a, b, c)
        differ = max_people - min_people
        if differ < min_differ:
            min_differ = differ
    else:
        dfs(index + 1, a + c_list[index], b, c)
        dfs(index + 1, a, b + c_list[index], c)
        dfs(index + 1, a, b, c + c_list[index])


dfs(0, 0, 0, 0)
print(min_differ)
