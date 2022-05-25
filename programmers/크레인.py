# https://programmers.co.kr/learn/courses/30/lessons/64061

# 배운 점
# index에 대한 부분. 2d의 list l에서 l[i]는 i번째 열을 의미함. 만일 l[i][j]를 쓴다면, i번째 행의 l번째 열을 의미.
# numpy에서는 2d array l은 l[:,:]를 통해서 행과 열을 뽑아낼 수 있음.
# 맨뒤를 뽑을때에 등을 사용할 수 있다는 부분 [-1]
# break를 통해서 흐름 제어가 가능한 부분


# 독자적인 방법으로 푼 풀이

import numpy as np


def solution(board, moves):
    output = []
    answer = 0
    board = np.array(board)
    for move in moves:
        temp = board[:, move-1]
        for idx, out in enumerate(temp):
            if out != 0:
                output.append(out)
                board[idx, move-1] = 0
                if output[-1:] == output[-2:-1]:
                    answer += 2
                    print(output)
                    output = output[:-2]
                break
    return answer


# 해답을 참고한 풀이
def solution(board, moves):
    answer = []
    output = []
    for move in moves:
        for idx in range(len(board)):
            if board[idx][move-1] != 0:
                output.append(board[idx][move-1])
                board[idx][move-1] = 0
                if output[-1:] == output[-2:-1]:
                    answer.append(output[-1])
                    output = output[:-2]
                break
    return len(answer) * 2
