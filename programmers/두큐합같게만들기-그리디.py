# https://school.programmers.co.kr/learn/courses/30/lessons/118667

from collections import deque


def solution(queue1, queue2):
    cnt = 0
    queue1, queue2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(queue1), sum(queue2)
    for _ in range(len(queue1) * 3):
        if sum1 > sum2:
            sum1 -= queue1[0]
            sum2 += queue1[0]
            queue2.append(queue1.popleft())
        elif sum1 < sum2:
            sum2 -= queue2[0]
            sum1 += queue2[0]
            queue1.append(queue2.popleft())
        else:
            return cnt
        cnt += 1
    return -1
