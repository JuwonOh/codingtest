# 대표값

import sys
sys.stdin = open("input.txt", "rt")
n = int(input())
student = list(map(int, input().split()))

mean = round(sum(student)/n, 0)
valmin = float('inf')
for a in range(n):
    eachmin = abs(mean - student[a])
    if eachmin < valmin:
        valmin, minnum = eachmin, a
    elif eachmin == valmin:
        if student[a] > student[minnum]:
            valmin, minnum = student[a], a

print(minnum+1, mean, student[minnum])
