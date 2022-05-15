
# time out solution
from collections import defaultdict


def solution(id_list, report, k):
    stop = []
    answer = [0] * len(id_list)
    dicReports = {id: [] for id in id_list}
    for i in set(report):
        reported = i.split(' ')
        stop.append(reported[1])
        dicReports[reported[1]].append(reported[0])

    stop = set([i for i in stop if stop.count(i) >= k])

    for key, value in dicReports.items():
        for s in stop:
            if s in value:
                answer[id_list.index(key)] += 1
    return answer

# solution


def solution(id_list, report, k):
    answer = [0] * len(id_list)
    # 중복되는 report를 제거해주기. point:동일한 유저에 대한 신고는 1번으로 제한.
    report = set(report)

    # 유저별로 신고한 아이디가 들어있는 dict{신고를 한 유저: 신고한 유저 목록}
    user_list_who_i_report = defaultdict(set)
    # 유저별로 신고당한 횟수가 들어 있는 사전 {신고를 당한 유저: 신고를 당한 횟수}
    num_of_reported = defaultdict(int)
    # 신고당한 유저의 목록
    suspended = []

    for r in report:
        do_report, be_reported = r.split()

        num_of_reported[be_reported] += 1
        user_list_who_i_report[do_report].add(be_reported)

        if num_of_reported[be_reported] == k:
            suspended.append(be_reported)
    # 줄바꿈에 주의.
    for s in suspended:
        for i in range(len(id_list)):
            if s in user_list_who_i_report[id_list[i]]:
                answer[i] += 1
    return answer
