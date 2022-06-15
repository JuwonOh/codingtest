import sys
sys.stdin = open("inflearn/mysolution/input.txt", "rt")

n = int(input())
m_list = [list(map(int, input().split())) for _ in range(n)]
m_list.sort(reverse=True)

cnt = 0
largest = 0

for i in m_list:
    if i[1] > largest:
        cnt += 1
        largest = i[1]
    print(cnt, largest)
