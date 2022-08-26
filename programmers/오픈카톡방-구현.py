# https://school.programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    user_dict = dict()
    actions = []

    for data in record:
        temp = data.split()
        if temp[0] in ("Enter", "Change"):
            user_dict[temp[1]] = temp[2]
        actions.append((temp[0], temp[1]))

    for action in actions:
        if "Enter" == action[0]:
            answer.append("{}님이 들어왔습니다.".format(user_dict[action[1]]))
        elif "Leave" == action[0]:
            answer.append("{}님이 나갔습니다.".format(user_dict[action[1]]))
    return answer


# 다른 solution

def solution(record):
    user_id = {EC.split()[1]: EC.split(
    )[-1] for EC in record if EC.startswith('Enter') or EC.startswith("Change")}
    return ["{}님이 들어왔습니다.".format(user_id[action.split()[1]]) if action.startswith("Enter") else "{}님이 나갔습니다.".format(user_id[action.split()[1]]) for action in record if not action.startswith("Change")]
