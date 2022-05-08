# 수 정렬하기

## N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
# 첫 숫자가 전체 입력 하는 숫자를 의미한다.
N = int(input())

l = []

for a in range(N):
    l.append(int(input()))

l.sort()

for a in range(N):
    print(l[a])