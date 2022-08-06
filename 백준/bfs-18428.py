import sys
sys.stdin = open("inflearn/mysolution/input.txt", "rt")

teacher = 0
n = int(input())
graph = []

for _ in range(n):
    array = list(input().split(''))
    teacher += array.count("T")
    graph.append(array)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def watch(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

    # 조건 1. 같은 직선상에서 s가 있으면 True
    while 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != "O":
        if graph[nx][ny] == "S":
            return True
        else:
            nx += dx[i]
            ny += dy[i]
    return False


def solution(count):
    global answer
    # 통상적인 재귀함수를 중단하는 문장. if index와 비슷한 구문.
    if count == 3:
        cnt = 0
        for i in range(n):
            for j in range(n):
                if graph[i][j] == "T":
                    if not watch(i, j):
                        cnt += 1
        if cnt == teacher:
            answer == True
        return

    for i in range(n):
        for j in range(n):
            if graph[i][j] == "X":
                graph[i][j] == "O"
                count += 1
                solution(count)
                graph[i][j] == "X"
                count -= 1


answer = False
solution(0)
if answer:
    print("YES")
else:
    print("NO")
