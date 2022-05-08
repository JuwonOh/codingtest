# 단어의 갯수

##문제
###영어 대소문자와 공백으로 이루어진 문자열이 주어진다. 이 문자열에는 몇 개의 단어가 있을까? 이를 구하는 프로그램을 작성하시오. 단, 한 단어가 여러 번 등장하면 등장한 횟수만큼 모두 세어야 한다.


words = input().split(' ')
print(len(words))

## 주의
### .split()과 .split(" ")은 다르다. https://somjang.tistory.com/entry/Python-%EB%AC%B8%EC%9E%90%EC%97%B4-split-%EA%B3%BC-split-%EC%B0%A8%EC%9D%B4-%EC%95%8C%EC%95%84%EB%B3%B4%EA%B8%B0

string = "a b d f     "
string.split()## 화이트 스페이스가 여러개 있어도 단어만 나눠준다.
string.split(' ')# 화이트 스테이스 하나씩 나눠준다.

