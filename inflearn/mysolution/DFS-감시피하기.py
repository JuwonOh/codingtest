
import sys
sys.stdin = open("inflearn/mysolution/input.txt", "rt")

teacher = 0
n = int(input())
graph = []

for _ in range(n):
    array = list(input().strip().split(' '))
    teacher += array.count("T")
    graph.append(array)
# 상하좌우 움직이기 -> 같은 열행에 T가 있으며 안된다.
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 한명이라도 학생을 볼 수 있으면 안된다.


def watch(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        while 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != "O":
            # 일직선상에 있는 학생을 다 살펴본다.
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
