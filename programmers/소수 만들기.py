# 소수 만들기
# 문제 설명
# 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. '
# 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때
# 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
# nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.
# 입출력 예
# nums	result
# [1,2,3,4]	1
# [1,2,7,6,4]	4
# 입출력 예 설명
# 입출력 예 #1
# [1,2,4]를 이용해서 7을 만들 수 있습니다.

# 입출력 예 #2
# [1,2,4]를 이용해서 7을 만들 수 있습니다.
# [1,4,6]을 이용해서 11을 만들 수 있습니다.
# [2,4,7]을 이용해서 13을 만들 수 있습니다.
# [4,6,7]을 이용해서 17을 만들 수 있습니다.

from abc import abstractmethod
from itertools import combinations


def isPrime(num):
    if num == 0:
        return 0
    for i in range(2, int(num/2)+1):
        if num % i == 0:
            return 0
    else:
        return 1


def solution(nums):
    answer = 0
    arr = list(combinations(nums, 3))
    print(arr)
    for i in arr:
        print(i[0]+i[1]+i[2])
        answer += isPrime(i[0]+i[1]+i[2])
    return answer

# 배운 점
# for else문을 사용할 수 있음에 주의
# for else문은 for가 끝난 뒤에, 마지막으로 특정한 행동을 해줌.
# for문을 돌릴때 조건을 충족하지 않는 경우에서 쉽게 사용할 수 있음.
# 에라토스테네스의 체를 쉽게 구현하는 이분 탐색 기법에 유의



     