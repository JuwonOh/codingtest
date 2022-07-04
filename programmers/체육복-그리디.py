##https://programmers.co.kr/learn/courses/30/lessons/42862
## 


def solution(n, lost, reserve):
    cnt =0 
    for x in lost:
        if x-1 in reserve:
            reserve.remove(x-1)
            cnt += 1
        elif x+1 in reserve:
            reserve.remove(x+1)
            cnt += 1
        elif x in reserve:
            reserve.remove(x)
            cnt += 1
        print(lost, reserve, cnt)
        
    answer = n- len(lost) +cnt
    return answer


def solution(n, lost, reserve):
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)

    for x in set_reserve:
        if x-1 in set_lost:
            set_lost.remove(x-1)
        elif x+1 in set_lost:
            set_lost.remove(x+1)

    answer = n- len(set_lost)
    return answer