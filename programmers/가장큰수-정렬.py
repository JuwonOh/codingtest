## https://school.programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    n_list = list(map(str, numbers))
    n_list = sorted(n_list, key = lambda x: x[0], reverse=True)
    res = "".join(n_list)
    return res