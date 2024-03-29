# 문제 설명

# A기업은 마케팅 계획을 수립하기 위해, 설문조사를 실시하였습니다. 취합된 설문지 중, 성의 없이 응답한 불량 설문지를 걸러내려고 합니다. 즉, 길이 n 이상의 응답패턴이 k번 이상 연속되면 불량 설문지로 간주하기로 했습니다. 예를 들어, A기업의 13가지 서비스에 대해서 만족도를 6가지 (A=매우 만족, B=만족, C=조금 만족, D=조금 불만족, E=불만족, F=매우 불만족)로 응답받았다고 가정합니다. 그리고 길이 3 이상의 응답패턴이 2회 이상 연속된 경우를 '불량 설문지'로 판단하기로 했다면 그 결과는 아래와 같습니다.
# 불량 기준 : 길이 3 이상인 응답패턴이 2회 이상 연속됨

# 설문지ID	설문 결과	불량 여부
# 1	AFFDEFDEFDEEC	불랑 : 길이 3인 응답패턴(FDE)이 3회 연속됨
# 2	ABABABABBCCEF	불량 : 길이 4인 응답패턴(ABAB)이 2회 연속됨
# 3	FFFFFFFFFFFFF	불량 : 길이 3인 응답패턴(FFF)이 4회 연속됨
# 4	FCBBBFCBBECBB	정상 : 길이 4인 응답패턴(FCBB)이 2회 나타났으나, 연속해서 나타나지는 않았음(중간에 B가 들어가 있음)
# 2번 설문지에서, 길이 2인 응답패턴(AB)이 4회 연속한 것으로 본다면 불량이 아닙니다. 하지만 패턴을 나눌 수 있는 모든 경우를 고려해서, 그중 하나라도 기준(길이 3 이상의 패턴이 2번 이상 반복)에 맞으면 불량이라고 판단해야 합니다.
# 3번 설문지에서, 길이 4인 응답패턴(FFFF)이 3회 연속된 것으로도 볼 수 있습니다. 물론 이 경우에도 불량의 기준에 맞습니다.
# 설문 결과를 담은 문자열 배열 replies, 불량의 기준이 되는 정수형 변수 n, k가 매개변수로 주어집니다. 이때, 각 설문지에 대해서, 불량/정상 여부를 배열에 담아서 return 하도록 solution 함수를 완성해주세요. 1번 설문지부터 마지막 설문지까지 검사해서 차례대로 불량이면 0, 정상이면 1을 담아서 return 합니다.

# 제한사항
# replies의 길이(=설문지의 개수)는 1 이상 100 이하입니다.
# replies의 원소는 응답자의 설문지를 나타냅니다.
# 1번 설문지부터 마지막 설문지까지의 결과가 차례대로 담겨 있습니다.
# replies의 원소는 길이 1 이상 400 이하인 문자열입니다.
# 즉, 설문 문항의 수는 1개 이상 400개 이하입니다.
# replies의 원소들의 길이는 모두 같습니다.
# replies의 원소는 'A' ~ 'F' 사이의 6개 대문자 알파벳으로만 이루어진 문자열입니다.
# n은 2 이상 설문 문항의 수 이하인 자연수입니다.
# k는 2 이상 설문 문항의 수 이하인 자연수입니다.
# 입출력 예
# replies	n	k	result
# ["AFFDEFDEFDEEC", "ABABABABBCCEF", "FFFFFFFFFFFFF", "FCBBBFCBBECBB"]	3	2	[0, 0, 0, 1]
# ["AFFDEFDEFDEEC", "ABABABABBCCEF", "FFFFFFFFFFFFF", "FCBBBFCBBECBB"]	2	4	[1, 0, 0, 1]
# ["FFCCAAFCCAAA", "AAAABBBBCCCC", "ABCABCABCABC"]	4	2	[0, 1, 0]
# ["FFCCAAFCCAAA", "AAAABBBBCCCC", "ABCABCABCABC"]	3	3	[1, 1, 0]
# 입출력 예 설명
# 입출력 예 #1
# 문제 예시와 같습니다.

# 입출력 예 #2
# 불량 기준 : 길이 2 이상인 응답패턴이 4회 이상 연속됨

# 설문지ID	설문 결과	불량 여부
# 1	AFFDEFDEFDEEC	정상
# 2	ABABABABBCCEF	불량 : 길이 2인 응답패턴(AB)가 4회 연속됨
# 3	FFFFFFFFFFFFF	불량 : 길이 3인 응답패턴(FFF)가 4회 연속됨
# 4	FCBBBFCBBECBB	정상
# 3번은 길이 2인 응답패턴(FF)가 6회 반복되어 불량이라고 판단할 수도 있습니다.
# 입출력 예 #3
# 불량 기준 : 길이 4 이상인 응답패턴이 2회 이상 연속됨

# 설문지ID	설문결과	불량 여부
# 1	FFCCAAFCCAAA	불량 : 길이 5인 응답패턴(FCCAA)가 2회 연속됨
# 2	AAAABBBBCCCC	정상
# 3	ABCABCABCABC	불량 : 길이 6인 응답패턴(ABCABC)가 2회 연속됨
# 입출력 예 #4
# 불량 기준 : 길이 3 이상인 응답패턴이 3회 이상 연속됨

# 설문지ID	설문결과	불량 여부
# 1	FFCCAAFCCAAA	정상
# 2	AAAABBBBCCCC	정상
# 3	ABCABCABCABC	불량 : 길이 3인 응답패턴(ABC)가 4회 연속됨


import re


def check(word, n, k):
    pattern = "(.{{{},}}?)".format(n) + "\\1" + "{{{}}}".format(k)
    print(pattern)
    r = re.compile(pattern)
    if r.search(word):
        print(0)
        return 0
    else:
        print(1)
        return 1


check("ABABABABBCCEF", 3, 2)
