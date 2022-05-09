import sys
sys.stdin = open("mysolution/input.txt", "rt")
n, m = map(int, input().split())
cnt = [0] * (n + m + 3)
max_val = 0
# 공식 solution
# for i in range(1, n + 1):  # 1부터 n까지 돌기 위해서.
#     for j in range(1, n + 1):
#         cnt[i+j] += 1
# for i in range(n + m + 1):
#     if cnt[i] > max_val:
#         max_val = cnt[i]

# for i in range(n + m + 1):
#     if cnt[i] == max_val:
#         print(i, end=" ")

# 느낀 점: 지나치게 무식한 solution이다. + range를 잘 다루자.

# 개인적인 해법
for i in range(1, n+1):
    for j in range(1, n+1):
        cnt[i+j] += 1

# max를 통해서 가장 큰 수를 찾자.
max_val = max(cnt)
print(max_val)
for a in range(len(cnt)):
    if cnt[a] == max_val:
        print(a, end=' ')
