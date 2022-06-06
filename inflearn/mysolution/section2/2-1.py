import sys
sys.stdin = open("input.txt", "rt")

N, K = map(int, input().split())
yag = []

for a in range(1, N):
    if N % a == 0:
        yag.append(a)
        continue
    if len(yag) == K:
        print(a)
        break
else:
    print(-1)
