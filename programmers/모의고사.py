def solution(answers):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt = [0, 0, 0]

    for idx, answer in enumerate(answers):
        if answer == a[idx % 5]:
            cnt[0] += 1
        if answer == b[idx % 8]:
            cnt[1] += 1
        if answer == c[idx % 10]:
            cnt[2] += 1

    max_val = max(cnt)
    res = []
    for i in range(3):
        if max_val == cnt[i]:
            res.append(i+1)
    return res
