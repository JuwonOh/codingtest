cnt = 0


def solution(numbers, target):
    def DFS(index, s_total):

        global cnt

        if index == len(numbers):
            if s_total == target:
                cnt += 1
        else:
            value = numbers[index]
            DFS(index + 1, s_total + value)
            DFS(index + 1, s_total - value)

    DFS(0, 0)
    return cnt
