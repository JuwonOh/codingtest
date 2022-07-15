import sys
sys.stdin = open("inflearn/mysolution/input.txt", "rt")

n, cd = map(int, input().split())
m_list = list(map(int, input().split()))

e = sum(m_list)
s = max(m_list)
res = 0


def select(threshold):
    cnt = 1
    sum_val = 0
    for i in m_list:
        sum_val += i
        if sum_val > threshold:
            cnt += 1
            sum_val = i
    return cnt


while s <= e:
    mid = (s+e)//2
    if mid > s and select(mid) > cd:
        s = mid + 1
    else:
        e = mid - 1
    print(s, e, select(mid), mid)
