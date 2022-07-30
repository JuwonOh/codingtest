import sys
import itertools as it
sys.stdin = open("inflearn/mysolution/input.txt", "rt")
n, k = map(int, input().split())
num_list = list(map(int, input().split()))
div = int(input())
cnt = 0

for tmp in it.combinations(num_list, k):
    if sum(tmp) % div == 0:
        cnt += 1
        print(tmp)

print(cnt)
