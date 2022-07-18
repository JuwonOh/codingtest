from collections import deque

bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]


def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    in_b = deque([0]*bridge_length)
    answer = bridge_length
    while truck_weights:
        answer += 1
        cur = in_b.popleft()
        if sum(in_b) + truck_weights[0] < weight:
            new = truck_weights.popleft()
            in_b.append(new)
        else:
            in_b.append(0)
        print(answer, in_b)
    return answer


solution(bridge_length, weight, truck_weights)
