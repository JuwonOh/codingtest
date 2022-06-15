import sys
sys.stdin = open("inflearn/mysolution/input.txt", "rt")

n = int(input())
a_list = [list(map(int, input().split())) for _ in range(n)]
a_list = sorted(a_list, key=lambda x: (x[1], x[0]))

cnt = 1
e = a_list[0][1]

for i in a_list:
    if i[0] >= e:
        cnt += 1
        e = i[1]
print(cnt)
