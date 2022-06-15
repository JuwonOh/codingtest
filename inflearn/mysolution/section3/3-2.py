import sys
sys.stdin = open("inflearn/mysolution/input.txt", "rt")

s = input()
num = ''


def num_yag(num):
    cnt = 1  # 약수로 1이 있기에 넣는다.
    for i in range(1, num//2+1):
        if num % i == 0:
            cnt += 1
    print(cnt)
    return cnt


for i in s:
    if i.isnumeric() is True:
        num += i
num = int(num)
num_yag(num)
