# https://school.programmers.co.kr/learn/courses/30/lessons/42885

def solution(limit, people):
    people = sorted(people)
    s = 0
    e = len(people)-1
    cnt = 0
    while s <= e:
        cnt += 1
        if people[s] + people[e] <= limit:
            s += 1
        e -= 1
    print(cnt)
    return cnt
