# 문제 설명
# 어떤 정수들이 있습니다. 이 정수들의 절댓값을 차례대로 담은 정수 배열 absolutes와 이 정수들의 부호를 차례대로 담은 불리언 배열 signs가 매개변수로 주어집니다. 실제 정수들의 합을 구하여 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# absolutes의 길이는 1 이상 1,000 이하입니다.
# absolutes의 모든 수는 각각 1 이상 1,000 이하입니다.
# signs의 길이는 absolutes의 길이와 같습니다.
# signs[i] 가 참이면 absolutes[i] 의 실제 정수가 양수임을, 그렇지 않으면 음수임을 의미합니다.
# 입출력 예
# absolutes	signs	result
# [4,7,12]	[true,false,true]	9
# [1,2,3]	[false,false,true]	0
# 입출력 예 설명
# 입출력 예 #1

# signs가 [true,false,true] 이므로, 실제 수들의 값은 각각 4, -7, 12입니다.
# 따라서 세 수의 합인 9를 return 해야 합니다.
# 입출력 예 #2

# signs가 [false,false,true] 이므로, 실제 수들의 값은 각각 -1, -2, 3입니다.
# 따라서 세 수의 합인 0을 return 해야 합니다.

def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i] == True:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer


def solution(absolutes, signs):
    return sum(absolutes if signs else - absolutes for absolutes, signs in zip(absolutes, signs))

# 배운 지점

# zip을 사용하는 방법. zip을 사용하면 같은 길이의 리스트 두개를 합쳐서 사용할 수 있다.
# 또한 for a,b in zip(a, b)와 같은 방법도, for pair in zip(a,b)와 같은 방법도 가용하다.
# list comprehension을 이용한 방법도 잘 찾아 보자.
# 또한 list comprehenstion과 if, else문이 조합 되었을때의 순서도 봐보자.
