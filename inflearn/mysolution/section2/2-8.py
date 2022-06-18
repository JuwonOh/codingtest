from re import T
import sys
sys.stdin = open("mysolution/input.txt", "r")
n = int(input())
a = list(map(int, input().split()))


def reverse(x):
    reverse_val = 0
    while x > 0:
        res = x % 10  # 나머지가 res
        reverse_val = reverse_val * 10 + res
        x = x // 10
    return reverse_val


def isPrime(x):
    if x == 0:
        return False
    for a in range(2, x//2 + 1):  # 절반만 돌면된다. 16을 2로 나누면, 2 *8 절반까지만 돌면 된다.
        if x % a == 0:  # i로 나누어 떨어지는 가?
            return False
    else:
        return True


for x in a:
    tmp = reverse(x)
    if isPrime(tmp):
        print(x)
