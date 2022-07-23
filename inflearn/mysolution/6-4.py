import sys
sys.stdin = open("inflearn/mysolution/input.txt", "rt")

n = int(input())
a_list = list(map(int, input().split()))
total = sum(a_list)


def DFS(L, sum):
    if sum > total / 2:
        return

    if L == n:
        if sum == (total - sum):
            print("Yes")
            sys.exit(0)
    else:
        DFS(L + 1, sum + a_list[L])  # l번째 수를 더한 경우.
        DFS(L + 1, sum)  # l번째 수를 안 더한 경우
