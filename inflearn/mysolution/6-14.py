import sys
sys.stdin = open("inflearn/mysolution/input.txt", "rt")

n, m = map(int, input().split())
# 목표 인접행렬을 만드는 것.
g = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    g[a][b] = 1
    g[b][a] = 1

print(g)
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(g[i][j], end=' ')
    print()


r = sys.stdin
n_num = map(int, input().split())
n_list = set(input().rstrip() for _ in range(n_num))
init = []
for i in n_list:
    init.append(n_list[i][0])

res = []
for key, value in init.items():
    if value >= 5:
        res.append(key)
res.sort()
if res:
    print(''.join(res))
else:
    print('PREDAJA')
