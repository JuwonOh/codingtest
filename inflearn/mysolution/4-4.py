import sys
sys.stdin = open("inflearn/mysolution/input.txt", "rt")

magu, horse = map(int, input().split())
coordinate = sorted([int(input()) for _ in range(magu)])

s = 1
e = max(coordinate)


def select(distance_two):
    cnt = 1
    sum_val = 0
    for i in coordinate:
        sum_val += i
        if sum_val > distance_two:
            cnt += 1
            sum_val = 0
    return cnt


while s <= e:
    distance = (s + e)//2
    if select(distance) < horse:
        e = distance - 1
    else:
        s = distance + 1
    print(s, e, distance, select(distance))
