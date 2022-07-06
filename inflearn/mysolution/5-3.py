import sys
sys.stdin = open("inflearn/mysolution/input.txt", "rt")

formula = input()
res = ''
stack = []
for i in formula:
    if i.isdecimal():
        res += i
    else:
        if i == "(":
            stack.append(i)
        elif i == "*" or i == "/":
            while stack and (stack[-1] == '*' or stack[-1] == "/"):
                res += stack.pop()
            stack.append(i)
        elif i == "+" or i == "-":
            while stack and stack[-1] != "(":
                res += stack.pop()
            stack.append(i)
        elif i == ")":
            while stack and stack[-1] != "(":
                res += stack.pop()
            stack.pop()
        print(stack)
while stack:
    res += stack.pop()
print(res)
