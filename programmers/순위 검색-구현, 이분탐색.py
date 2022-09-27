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
