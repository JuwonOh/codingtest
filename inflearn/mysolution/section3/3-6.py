import sys
sys.stdin = open("inflearn/mysolution/input.txt", "rt")

n = int(input())
m = []
res = []
dia1 = 0
dia2 = 0

# view matrix
m = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    # sum row
    res.append(sum(m[i][:]))
    # sum col
    res.append(sum(m[:][i]))
    # sum diagonal
    dia1 += m[i][i]
    dia2 += m[i][n-i-1]

res.append(dia1)
res.append(dia2)
res = sorted(res, reverse=True)
print(res)

# 답안
# 별로임

largest = -214700000

for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += m[i][j]
        sum2 += m[j][i]

    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2
sum1 = sum2 = 0

for i in range(n):
    sum1 += m[i][i]
    sum2 += m[i][n-i-1]
if sum1 > largest:
    largest = sum1
if sum2 > largest:
    largest = sum2
