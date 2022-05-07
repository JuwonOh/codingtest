# K번째 수
# 조건 같은 숫자의 카드가 여러장 가능
# 여기에서 3장을 뽑아서 각 카드에 적힌 수를 합한 값을 기록
# 기록한 값에서 k번째로 큰 수를 출력

# 문제: list내에서 중복된 수가 들어갈 수 있다.

import sys
sys.stdin = open("input.txt", "rt")
n, k = map(int, input().split())
a = list(map(int, input().split()))
res = set()

for tmp1 in range(n):
    for tmp2 in range(tmp1, n):
        for tmp3 in range(tmp2, n):
            res.add(a[tmp1] + a[tmp2] + a[tmp3])

res = list(res)
res.sort(reverse=True)
print(res)
