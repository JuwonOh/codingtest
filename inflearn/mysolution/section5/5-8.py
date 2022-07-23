import sys

sys.stdin = open("inflearn/mysolution/input.txt", "rt")

n = int(input())

word_list = [input() for _ in range(n)]

for _ in range(n-1):
    p_word = input()
    word_list.remove(p_word)
print(word_list[0])

# dict를 사용해서 문제를 풀어보기

word_dict = {input(): 1 for i in range(n)}

for _ in range(n-1):
    word_dict[input()] -= 1
print(word_dict)
