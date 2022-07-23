from itertools import permutations


def sosu(number):
    if number < 2:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


def solution(num):
    res = []
    for i in range(1, len(num)+1):
        res.extend(permutations(num, i))
    temp = set(int("".join(i)) for i in res)
    cnt = 0
    for i in temp:
        if sosu(i):
            cnt += 1

    return cnt
