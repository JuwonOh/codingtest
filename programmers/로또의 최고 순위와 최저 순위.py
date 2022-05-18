def solution(lottos, win_nums):
    dict = {'6': 1, '5': 2, '4': 3, '3': 4, '2': 5, '1': 6, '0': 6}
    cnt = 0
    max_cnt = 0
    for idx, num in enumerate(lottos):
        if num in win_nums:
            cnt += 1
            max_cnt += 1
            print(cnt, num)
        elif num == 0:
            max_cnt += 1

    answer = sorted([dict[str(cnt)], dict[str(max_cnt)]])
    return answer
# 다른 풀이방법


def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans], rank[ans]
