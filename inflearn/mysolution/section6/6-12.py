import sys
import itertools as it
sys.stdin = open("inflearn/mysolution/input.txt", "rt")
n, f = map(int, input().split())
b = [1] * n
for i in range(1, n):
    b[i] = b[i-1] * (n-i) / i
a = list(range(1, n + 1))
cnt = 0

for tmp in it.permutations(a):
    sum = 0
    for index, x in enumerate(tmp):
        # index를 통해서 이항계수를 곱하기 위해서 사용
        sum += (x * b[index])
    if sum == f:
        cnt += 1
        for x in tmp:
            print(x, end=' ')
        print()
print(cnt)
