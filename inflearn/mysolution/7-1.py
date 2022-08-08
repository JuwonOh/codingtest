import sys
sys.stdin = open("inflearn/mysolution/input.txt", "rt")

n, m = map(int, input().split())
q_list = [list(map(int, input().split())) for _ in range(n)]
max_score = 0


def dfs(index, t_score, t_time):
    global max_score
    if t_time > m:
        return
    if index == n:
        if max_score < t_score:
            max_score = t_score
    else:
        dfs(index + 1, t_score + q_list[index][0], t_time + q_list[index][1])
        dfs(index + 1, t_score, t_time)


dfs(0, 0, 0)
print(max_score)
