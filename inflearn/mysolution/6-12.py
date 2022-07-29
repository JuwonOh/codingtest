import sys
import itertools as it
sys.stdin = open("inflearn/mysolution/input.txt", "rt")
n, f = map(int, input().split())
cnt = 0
b = [1] * n
for i in range(1, n):
    b[i] = b[i-1] * (n-1) / i

a = list(range(1, n+1))

for tmp in it.permutations(a):
    t_sum = 0
    for index, x in enumerate(tmp):
        t_sum += (x * b[index])
        if t_sum == f:
            for x in tmp:
                print(x, end=' ')
            print(t_sum)
            break
