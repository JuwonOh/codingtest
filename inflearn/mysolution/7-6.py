import sys
import string
sys.stdin = open("inflearn/mysolution/input.txt", "rt")

code = input()
n = len(code)
code = code + "9"
cnt = 0
alpha = string.ascii_uppercase
word = ""
res = []


def dfs(index, position):
    global word, res, cnt
    if index == n:
        cnt += 1
        res.append(word)
        word = ""

    else:
        for i in range(0, len(alpha)):
            # index가 1의 자리수인 경우.
            if i == int(code[index]):
                word += alpha[i]
                print(i, index)
                dfs(index + 1, position + 1)
            # index가 십의 자리 수인 경우.
            elif len(str(i)) == 2 and code[index] == i//10 and code[index+1] == i % 10:
                word += alpha[i]
                print(i, index)
                dfs(index+2, position + 1)


dfs(0, 0)
print(cnt, word, res)
