import sys
sys.stdin = open("inflearn/mysolution/input.txt", "rt")

a_len = int(input())
a = list(map(int, input().split()))
b_len = int(input())
b = list(map(int, input().split()))

# while을 사용한 더 어려운 풀이.

p1 = 0
p2 = 0
c = []

while p1 < a_len and p2 < b_len:
    if a[p1] <= b[p2]:
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1

print(c)
