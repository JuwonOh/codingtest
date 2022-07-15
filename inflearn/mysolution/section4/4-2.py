import sys
sys.stdin = open("inflearn/mysolution/input.txt", "rt")

m, n = map(int, input().split())
lan_list = sorted([list(map(int, input().split()))[0] for _ in range(m)])
s = 0
e = lan_list[-1]

while s <= e:
    cnt = 0
    mid = (s + e) // 2
    for i in lan_list:
        cnt += i // mid
    if cnt < n:
        e = mid-1
    else:
        s = mid+1
    print(s, e, mid, cnt)
