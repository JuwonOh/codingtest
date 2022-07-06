import sys
sys.stdin = open("inflearn/mysolution/input.txt", "rt")

pipes = input()

stack = []
pieces = 0
for pipe in pipes:
    stack.append(pipe)
    if stack[-1] == ")":
        stack.pop()
        stack.pop()
        pieces += len(stack)

print(pieces)
