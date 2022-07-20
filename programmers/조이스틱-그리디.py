# https://school.programmers.co.kr/learn/courses/30/lessons/42860

def solution(name):

    min_move = len(name) - 1
    answer = 0

    for i, alp in enumerate(name):
        answer += min(ord(alp) - ord("A"), ord('Z') - ord(alp)+1)

        next = i + 1
        while next < len(name) and name[next] == "A":
            next += 1

        min_move = min([min_move, 2 * i + len(name) -
                       next, i + 2 * (len(name) - next)])
    answer += min_move
    return answer


solution("JUWON")
