# K번째 수
# 조건 같은 숫자의 카드가 여러장 가능
# 여기에서 3장을 뽑아서 각 카드에 적힌 수를 합한 값을 기록
# 기록한 값에서 k번째로 큰 수를 출력

# 문제: list내에서 중복된 수가 들어갈 수 있다.

import sys
sys.stdin = open("inflearn/mysolution/input.txt", "rt")
n, k = map(int, input().split())
a_list = list(map(int, input().split()))
res = set()

for a in range(n):
    for b in range(a, n):
        for c in range(b, n):
            res.add(a_list[a] + a_list[b] + a_list[c])

res = list(res)
res.sort(reverse=True)
print(res[k-1])
