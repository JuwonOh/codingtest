
import sys
sys.stdin = open("inflearn/mysolution/input.txt", "rt")

n = int(input())
check = [0] * (n + 1)


def DFS(v):
    # 종료지점에 온 것.
    if v == n + 1:
        for i in range(1, n + 1):
            if check[i] == 1:
                print(i, end=' ')
        print()

    else:
        # 종료지점에 오기 이전에 stack에 하나씩 쌓아나간다.
        # 원소를 부분집합으로 사용한다.
        check[v] = 1
        # 먼저 dfs를 하나씩 넘어감.
        DFS(v + 1)
        # back을 해서 하나씩 넘어간다.
        check[v] = 0
        # 마지막 자리 n이 3이면, v가 4. 일때 check list에서 1인 것들만 print
        DFS(v + 1)


DFS(1)
