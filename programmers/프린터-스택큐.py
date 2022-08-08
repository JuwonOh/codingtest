from collections import deque
priorities = [1, 1, 9, 1, 1, 1]
location = 4

# 배운 점: 사실 inflearn 응급실 문제와 아예 동일
# 하지만 enumrate나 논리 구조에서의 해답을 이끌어 내지 못함


def solution(priorities, location):
    cnt = 0
    pr_list = deque((num, pr) for num, pr in enumerate(priorities))

    while pr_list:
        cur = pr_list.popleft()
        if any(cur[1] < x[1] for x in pr_list):
            pr_list.append(cur)
        else:
            cnt += 1
            if cur[0] == location:
                print(cnt)
                break


solution(priorities, location)


from collections import deque

def solution(priorities, location):
	cnt = 0
	priorities = deque((num, pri) for num, pri in enumerate(priorities))
	while priorities:
		cur = priorities.popleft
		if any(cur[1] < x[1] for x in priorities):
			priorities.append(cur)
		else:
			cnt += 1
			if cur[0] == location:
				print(cnt)
				break