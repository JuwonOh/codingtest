# 자릿수의 합
import sys
sys.stdin = open("mysolution/input.txt", "r")
n = int(input())
a = list(map(int, input().split()))


def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x = x // 10
    return sum

# 다른 solution


def digit_sum(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    return sum


max_val = 0
for x in a:
    tot = digit_sum(x)
    if tot > max_val:
        max_val = tot
        res = x

print(res)
