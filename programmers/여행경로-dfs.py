
from collections import defaultdict
tickets = [["ICN", "SFO"], ["ICN", "ATL"], [
    "SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]


def solution(tickets):
    answer = ["ICN"]
    remained_list = []

    def dfs(start, tickets):
        if not tickets:
            return
        temp_dict = {}

        for i, ticket in enumerate(tickets):
            # 만일 출발지점으로 지정된 곳과 일치하면
            if ticket[0] == start:
                # temp dict에 넣어서 후보 도착지로 정함
                # index를 value로 도착지가 key로 들어간다.
                temp_dict[ticket[1]] = i
        print(temp_dict, tickets, remained_list, answer)
        # 후보 도착지가 없다면
        if len(temp_dict) == 0:
            # 잘못된 경로로 들어간다면, answer로 들어갔던 것을 취소하고, remain에 넣는다.
            remained_list.append(answer.pop())
            # 출발지는 직전 노드로 돌아간다.
            dfs(answer[-1], tickets)
        else:
            # 도착지가 있다면, 후보 dict를 정렬한다.
            temp_dict = sorted(temp_dict.items(), key=lambda item: item[0])
            # ticket은 후보 도착지이다.
            ticket = temp_dict[0][0]
            # answer에는 후보 도착지가 들어가 있다.
            answer.append(ticket)
            # idx에는 전체 ticket에서 후보 도착지의 순서가 있다.
            idx = temp_dict[0][1]
            # 한번 후보로 들어가면, 전체 ticket에서 사라진다.
            del tickets[idx]
            print(ticket, tickets)
            ##
            dfs(ticket, tickets)
    dfs("ICN", tickets)

    if len(remained_list) > 0:
        while remained_list:
            answer.append(remained_list.pop())
    return answer


tickets = [["ICN", "SFO"], ["ICN", "ATL"], [
    "SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]


def init_graph():
    routes = defaultdict(list)
    for key, value in tickets:
        routes[key].append(value)
    return routes


routes = init_graph()
print(routes)
