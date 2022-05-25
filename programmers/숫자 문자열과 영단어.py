# 네오와 프로도가 숫자놀이를 하고 있습니다. 네오가 프로도에게 숫자를 건넬 때 일부 자릿수를 영단어로 바꾼 카드를 건네주면 프로도는 원래 숫자를 찾는 게임입니다.

# 다음은 숫자의 일부 자릿수를 영단어로 바꾸는 예시입니다.

#     1478 → "one4seveneight"
#     234567 → "23four5six7"
#     10203 → "1zerotwozero3"

# 이렇게 숫자의 일부 자릿수가 영단어로 바뀌어졌거나, 혹은 바뀌지 않고 그대로인 문자열 s가 매개변수로 주어집니다. s가 의미하는 원래 숫자를 return 하도록 solution 함수를 완성해주세요.

# 참고로 각 숫자에 대응되는 영단어는 다음 표와 같습니다.
# 숫자 	영단어
# 0 	zero
# 1 	one
# 2 	two
# 3 	three
# 4 	four
# 5 	five
# 6 	six
# 7 	seven
# 8 	eight
# 9 	nine
# 제한사항

#     1 ≤ s의 길이 ≤ 50
#     s가 "zero" 또는 "0"으로 시작하는 경우는 주어지지 않습니다.
#     return 값이 1 이상 2,000,000,000 이하의 정수가 되는 올바른 입력만 s로 주어집니다.

# 입출력 예
# s 	result
# "one4seveneight" 	1478
# "23four5six7" 	234567
# "2three45sixseven" 	234567
# "123" 	123
# 입출력 예 설명

# 입출력 예 #1

#     문제 예시와 같습니다.

# 입출력 예 #2

#     문제 예시와 같습니다.

# 입출력 예 #3

#     "three"는 3, "six"는 6, "seven"은 7에 대응되기 때문에 정답은 입출력 예 #2와 같은 234567이 됩니다.
#     입출력 예 #2와 #3과 같이 같은 정답을 가리키는 문자열이 여러 가지가 나올 수 있습니다.

# 입출력 예 #4

#     s에는 영단어로 바뀐 부분이 없습니다.


# ## isdigit과 isnum을 사용해서 문자열을 다루는 기술
# ### 기억할 point
# 1. dict를 사용해서 넣는 방법
#     dict를 만들고, for idx, num in enumerate를 사용해서 dict에 key와 value를 넣는다.
#     또 if a == dict.keys():
#         temp += str(dict[key])
#     도 유용하다.
# 2. 빈 객체를 넣고 갱신하는 방법
#     isdigit, isalpha를 통해서 각 객체를 넣고, 그 객체를 하나씩 빼서 넣는 방법을 고려


# ## if a in b와 replace를 사용하는 방법
# ### 기억할 point
# 1. if a in b를 잘 사용하는 방법을 기억하기
#     if a in b를 사용하면 for문을 사용해서 b를 돌린다는 전제하에서, 내부에서 객체를 확인할 수 있음
# 2. replace처럼 특정 목적으로 만들어진 함수를 알면 더 쉽게 바꾸는게 가능하다.

# dict와 isalpha를 사용한 solution
def solution(s):
    dict = {}
    en = ["zero", "one", "two", "three", "four",
          "five", "six", "seven", "eight", "nine"]
    alpha_to_num = ""
    each_num = ''
    for idx, num in enumerate(en):
        dict[num] = idx
    for i in s:
        if i.isdigit():
            each_num += i
        if i.isalpha():
            alpha_to_num += i
            if alpha_to_num in dict.keys():
                each_num += str(dict[alpha_to_num])
                alpha_to_num = ''
    return int(each_num)


# if와 replace를 사용한 방법

def solution(s):
    en = ["zero", "one", "two", "three", "four",
          "five", "six", "seven", "eight", "nine"]
    answer = ''
    for idx, num in enumerate(en):
        if num in s:
            s.replace(num, idx)
    return s
