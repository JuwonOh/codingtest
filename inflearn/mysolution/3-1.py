import sys

sys.stdin = open("inflearn/mysolution/input.txt", "rt")
n = input()
for i in range(int(n)):
    sentence = input().lower()
    for size in range(len(sentence)):
        if sentence[size] != sentence[-1 - size]:
            print("#{} No".format(i + 1))
            break
    else:
        print("#{} Yes".format(i + 1))

## 더 pythonic하게
sys.stdin = open("inflearn/mysolution/input.txt", "rt")
n = input()

for i in range(int(n)):
    sentence = input().lower()
    if sentence == sentence[::-1]:
        print("#{} pass".format(i + 1))
else:
    print("fail")
