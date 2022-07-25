import sys
sys.stdin = open("inflearn/mysolution/input.txt", "rt")

n = int(input())
a_list = list(map(int, input().split()))
total = sum(a_list)

print(total)


def DFS(index, t_sum):
    if t_sum > total // 2:
        return
    if n == index:
        if t_sum == (total - t_sum):
            print("Yes")
            sys.exit(0)
    else:
        DFS(index + 1, t_sum + a_list[index])
        DFS(index + 1, t_sum)


DFS(0, 0)
