import sys
sys.stdin = open("inflearn/mysolution/input.txt", "rt")

# matix의 크기
n = int(input())
# matrix
m = [list(map(int, input().split())) for _ in range(n)]
# matrix의 중심
idx = n//2

res = []

for i in range(n):
    if i <= idx:
        # start는 6에서 시작되어 0이 되어야 한다.
        s = idx-i
        # end는 8에서 15가 되어야 한다.
        e = idx+i+1
        print(i, s, e, m[i][s:e])
        res.extend(m[i][s:e])
    else:
        # 하단부의 start는 -14에서 -8이 되어야 한다.
        s = i-n - idx
        # 하단부의 end는 -1에서 -7이 되어야 한다.
        e = idx-i
        print(i, s, e, m[i][s:e])
        res.extend(m[i][s:e])
print(sum(res))

# 다른 풀이방법

s = e = n//2
res = 0
for i in range(n):
    for j in range(s, e+1):
        res += m[i][j]
        print(i, j, m[i][j])
    if i < n // 2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1
