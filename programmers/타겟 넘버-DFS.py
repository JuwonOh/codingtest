cnt = 0


def solution(numbers, target):
    def DFS(index, t_sum):
        global cnt
        if index == len(numbers):
            if t_sum == target:
                cnt += 1
        else:
            value = numbers[index]
            DFS(index + 1, t_sum + value)
            DFS(index + 1, t_sum - value)

    DFS(0, 0)
    return cnt
