import sys
sys.stdin = open("inflearn/mysolution/input.txt", "rt")

n, k = map(int, input().split())
n_list = list(map(int, input().split()))
divided = int(input())
res = [0] * (k + 1)
temp = []


def DFS(index, sequence):
    num = 0
    if k == index:
        for j in range(k):
            num += res[j]
        if num % divided == 0:
            temp.append(num)
    else:
        for i in range(sequence, n):
            res[index] = n_list[i]
            DFS(index+1, i + 1)


DFS(0, 0)
print(temp, len(temp))
