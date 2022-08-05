# https://programmers.co.kr/learn/courses/30/lessons/42862
# https://www.notion.so/95eac0a5d0b241adb462c11b9a0bc034


def solution(n, lost, reserve):
    cnt = 0
    for x in lost:
        if x in reserve:
            reserve.remove(x)
            cnt += 1

        elif x+1 in reserve:
            reserve.remove(x+1)
            cnt += 1
        elif x-1 in reserve:
            reserve.remove(x-1)
            cnt += 1
    print(lost, reserve, cnt)
    answer = n - len(lost) + cnt
    return answer


def solution(n, lost, reserve):
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)

    for x in set_reserve:
        if x-1 in set_lost:
            set_lost.remove(x-1)
        elif x+1 in set_lost:
            set_lost.remove(x+1)

    answer = n - len(set_lost)
    return answer


def solution(n, lost, reserve):
    answer = n - len(lost)

    for i in range(len(reserve)):
        a = int(reserve[i])
        for j in range(len(lost)):
            b = int(lost[j])
            if a == b:
                a -= a
                b -= b
                answer += 1
            elif a - 1 == b and a + 1 == b:
                answer += 1
                a -= a
                b -= b
            elif a - 1 == b or a + 1 == b:
                answer += 1
                a -= a
                b -= b

    return answer
