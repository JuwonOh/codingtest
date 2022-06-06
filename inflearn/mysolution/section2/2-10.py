import sys

sys.stdin = open("inflearn/mysolution/input.txt", "rt")
n = int(input())
score_list = list(map(int, input().split()))

cnt = 1
if score_list[0] == 1:
    score = 1
else:
    score = 0
for idx in range(1, n):
    if score_list[idx] == score_list[idx - 1] and score[idx] == 1:
        cnt += 1
        score += cnt * 1
    else:
        cnt = 0
    print(score, cnt)

## 더 간단한 방식

sum = 0
cnt = 0

for x in score_list:
    if x == 1:
        cnt += 1
        sum += cnt
    else:
        cnt = 0

print(sum)

