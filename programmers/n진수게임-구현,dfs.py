# https://school.programmers.co.kr/learn/courses/30/lessons/17687

n, t, m, p = 2, 4, 2, 1

def convert(num, geesu):
    nums = "01234567890ABCDEF"
    q, r = divmod(num, geesu)
    if q == 0:
        return nums[r]
    else:
        print(q, geesu)
        return convert(q, geesu) + nums[r]

def solution(n, t, m, p):
    answer = ""
    temp = ""
    for i in range(t * m):
        temp += convert(i, n)
    for j in range(t):
        answer += temp[p - 1 + m*j]
    return answer

solution(n, t, m, p)
