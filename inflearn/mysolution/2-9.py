import sys

sys.stdin = open("inflearn/mysolution/input.txt", "rt")
n = int(input())
res = 0
for i in range(n):
    nums = sorted(input().split(), reverse=True)
    a, b, c = map(int, nums)
    if a == b and b == c:
        money = 10000 + a * 1000
    elif a == b:
        money = 1000 + a * 100
    elif b == c:
        money = 1000 + 100 * c
    else:
        money = a * 100

    if money > res:
        res = money

print(res)

