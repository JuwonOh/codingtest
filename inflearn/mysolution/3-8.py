import sys
sys.stdin = open("inflearn/mysolution/input.txt", "rt")

# matix의 크기
n = int(input())

m = [list(map(int, input().split())) for _ in range(n)]

change_n = int(input())

change_m = []
for i in range(change_n):

    modifiy_list = list(map(int, input().split()))

    # print(modifiy_list)
    # print(m[modifiy_list[0]-1])

    if modifiy_list[1] == 1:
        m[modifiy_list[0]-1] = m[modifiy_list[0]-1][n - modifiy_list[2]:] + \
            m[modifiy_list[0]-1][:n - modifiy_list[2]]
    else:
        m[modifiy_list[0]-1] = m[modifiy_list[0]-1][-n + modifiy_list[2]:] + \
            m[modifiy_list[0]-1][:-n + modifiy_list[2]]
    # print(m[modifiy_list[0]-1])

s = 0
e = n
res = 0

for a in range(n):
    for i in range(s, e):
        res += m[a][i]
    #print(a, s, e, res)
    # print(n//2)
    #print(res, a, i, s, e)
    if a < n // 2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
print(res)
