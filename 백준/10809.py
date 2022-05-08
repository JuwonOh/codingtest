# 알파벳 찾기

##문제
### 알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

S = input()
abc = "abcdefghijklmnopqrstuvwxyz"

for a in abc:
    if a in S:
        print(S.index(a), end= ' ')
    else:
        print(-1, end = " ")

## str.index(element)는 element가 str나 list의 몇번째 index에 있는지를 찾아준다.
## ex) a = [10,1,30,20] a.index(30) => 2
