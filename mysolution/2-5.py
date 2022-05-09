import sys
sys.stdin = open("mysolution/input.txt", "rt")
n, m = map(int, input().split())
cnt = [0] * (n + m + 3)
max_val = 0
# 공식 solution
# for i in range(1, n + 1):  # 1부터 n까지 돌기 위해서.
#     for j in range(1, m + 1):
#         cnt[i+j] += 1
# for i in range(n + m + 1):
#     if cnt[i] > max_val:
#         max_val = cnt[i]
# print(cnt)
# for i in range(n + m + 1):
#     if cnt[i] == max_val:
#         print(i, end=" ")

# 느낀 점: 지나치게 무식한 solution이다. + range를 잘 다루자.

# 개인적인 해법
for i in range(1, n+1):
    for j in range(1, m+1):  # 여기에서 m을 넣어서 실패했다. 주의해라.
        cnt[i+j] += 1

# max를 통해서 가장 큰 수를 찾자.
max_val = max(cnt)
print(cnt)
for a in range(len(cnt)):
    if cnt[a] == max_val:
        print(a, end=' ')
# enumerate를 통해서 해결하는 방법도 가능하다.

a_list = [index for index, item in enumerate(cnt) if item == max(cnt)]
print(a_list)


sys.stdin = open("mysolution/input.txt", "rt")
n, m = map(int, input().split())
cnt = [0] * (n+m+3)

for i in range(1, n + 1):
    for j in range(1, m + 1):
        cnt[i+j] += 1
