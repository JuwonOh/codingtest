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
    global word, cnt
    if index == n:
        cnt += 1
        print(word)
        res.append(word)
        word = ""

    else:
        for i in range(1, len(alpha)+1):
            print(i, int(code[index]), i == int(code[index]))
            # index가 1의 자리수인 경우.
            if i == int(code[index]):
                word += alpha[i-1]
                print(word, index)
                dfs(index + 1, position + 1)
            # index가 십의 자리 수인 경우.
            # code가 str이기 때문에, code[index]도 str이다. 자료형에 주의할 것.
            if len(str(i)) == 2 and int(code[index]) == i//10 and int(code[index+1]) == i % 10:
                word += alpha[i-1]
                dfs(index+2, position + 1)


dfs(0, 0)
print(cnt, word, res)
