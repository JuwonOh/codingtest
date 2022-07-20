# https://school.programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    people = sorted(people)
    cnt = 0
    s = 0
    l = len(people) - 1
    while s <= l:
        cnt += 1
        if people[s]+people[l] <= limit:
            s += 1
        l -= 1
    return cnt
