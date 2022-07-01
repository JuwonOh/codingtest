## 문제: https://programmers.co.kr/learn/courses/30/lessons/42586?language=python3

## 배운점
### 1. list내의 element를 더하는 과정: [sum(x) for x in zip(a_list, b_list)]
### 2. while을 다룰때, "while a 조건일때 작동"으로 이해
### 3. pop(위치)를 사용해서 앞부터 list의 element를 빼는게 가능.


cnt_list = []

def solution(progresses, speeds):
    while progresses:
        progresses = [sum(x) for x in zip(progresses, speeds)]
        
        cnt = 0
        while progresses and progresses[0] >= 100:
             progresses.pop(0)
             speeds.pop(0)
             cnt += 1
        if cnt >=1:
            cnt_list.append(cnt)
    print(cnt_list)
    return cnt_list

#progresses = [95, 90, 99, 99, 80, 99]
#speeds = [1, 1, 1, 1, 1, 1]
solution(progresses, speeds)