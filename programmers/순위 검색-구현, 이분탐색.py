def check(input, condition, idx):
    if condition == "-":
        return True
    elif idx == 4:
        if int(input) >= int(condition):
            return True
        else:
            return False
    else:
        if input == condition:
            return True
        else:
            return False


def solution(info, query):
    info = [i.split() for i in info]
    query = [i.replace('and ', '').split() for i in query]
    answer = []
    for o_query in query:
        cnt = 0
        for person in info:
            for idx, temp in enumerate(zip(person, o_query)):
                if check(temp[0], temp[1], idx) == False:
                    break
            else:
                cnt += 1
        answer.append(cnt)
    return answer

# 효율성을 달성할 수 있는 방법


def solution(info, query):
    data = dict()
    for a in ["cpp", "java", "python", "-"]:
        for b in ["backend", "frontend", "-"]:
            for c in ["junior", "senior", "-"]:
                for d in ["chicken", "pizza", "-"]:
                    data.setdefault((a, b, c, d), list())

    for i in info:
        i = i.split()
        for a in [i[0], "-"]:
            for b in [i[1], "-"]:
                for c in [i[2], "-"]:
                    for d in [i[3], "-"]:
                        data[(a, b, c, d)].append(int(i[4]))
    for k in data:
        data[k].sort()

    answer = list()
    for q in query:
        q = q.split()

        pool = data[(q[0], q[2], q[4], q[6])]
        find = int(q[7])
        l = 0
        r = len(pool)
        mid = 0
        while l < r:
            mid = (r + l)//2
            if pool[mid] >= find:
                r = mid
            else:
                l = mid + 1
        answer.append(len(pool)-1)
    return answer
