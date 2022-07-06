import sys
sys.stdin = open("inflearn/mysolution/input.txt", "rt")

num, m = map(int, input().split())

# str을 통해서 전체 수를 list로 만든다.
num = list(str(num))

res = []
for number in num:
    while m > 0 and res and res[-1] < number:
        res.pop()
        m -= 1
    res.append(number)
answer = ''.join(res)[:len(res)-m]
print(answer, res, m)
