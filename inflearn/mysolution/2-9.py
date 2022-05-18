import sys
sys.stdin = open("mysolution/input.txt")
n = int(input())
res = 0
for i in range(n):
    temp = input().split()
    temp.sort()
    a, b, c = map(int, temp)

    if a == b and b == c:
        money = 10000 + 1000 * c
    elif a == b or a == c:
        money = 1000 + 100 * a
    elif b == c:
        money = 1000 + 100 * c
    else:
        money * c
    if money > res:
        res = money
print(res)
