import sys
sys.stdin = open("inflearn/mysolution/input.txt", "rt")

n, k = map(int, input().split())
n_list = list(map(int, input().split()))
divided = int(input())
res = [0] * (k + 1)
temp = []

def DFS(index, sequence):
    t_sum = 0
    if index == k:
        for j in range(k):
            t_sum += res[j]
        if t_sum % divided == 0:
            temp.append(t_sum)

    else:
        for i in range(sequence, n):
            res[index] = n_list[i]
            DFS(index + 1, i + 1)


DFS(0, 0)
print(temp, len(temp))
