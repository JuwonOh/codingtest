from collections import deque
import sys
sys.stdin = open("inflearn/mysolution/input.txt", "rt")

n = int(input())


def r_f(n):
    if n == 0:
        return
    else:
        r_f(n//2)
        print(n % 2, end='')


r_f(n)
