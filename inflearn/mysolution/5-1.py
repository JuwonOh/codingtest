import sys
sys.stdin = open("inflearn/mysolution/input.txt", "rt")

num, m = map(int, input().split())

# str을 통해서 전체 수를 list로 만든다.
num = list(map(int, str(num)))

stack = []

for x in num:
    while stack and m > 0 and x > stack [-1]:
        stack.pop()
        m -= 1
    stack.append(x)
if m != 0:
    stack = stack[:-m]
res = ''.join(map(str, stack))
print(res)