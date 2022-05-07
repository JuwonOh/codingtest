## 시간제한, 메모리 제한을 확인하기
- 어떤 이유에서 코드의 실행시간이 오래 걸리는가: 연산량
- 계산량은 입력과 큰 관계를 가진다.

ex) sum으로 연산량을 알아보자. 
- 곱샘과 합연산은 다르다. 또한 ^연산은 더 오래걸린다.
- 모든 연산의 횟수가 다르다.
  
## Big-O notation
- O(1):
def sum_n(N):
    return N(N+1)//2

- O(N): 길이 N 수열에서 수 K 찾기
def search(1st, N, K):
    for i in 1st:
        if i == 1st : return True
    return False

- O(logN): 이분탐색. 길이가 절반으로 줄어든다.

def binary_search(lst, N, K):
    lo, hi = 0, N-1
    while lo <= hi :
        mid = (lo + hi) // 2
        if lst[mid] == K : return True
        if lst[mid] > K: hi = mid-1
        else : lo = mid+1
    return False

### BigO notation은 점근적 표현법이다. 시간과 공간에서 다룰 수 있음. 
- 시간 제한이 1초면 max(N) = 10억 O(N)이상의 알고리즘을 사용하면 안된다. 
  - 어떻게 하면 풀이를 간단하게 할 수 있을지 고민해봐야 한다.
- 해법: Naive한 풀이 떠올리기

ex)1부터 N까지의 수를 만든 수가 몇자리 수인지 찾는 프로그램

- 너무 복잡한 풀이 : 시간 복잡도가 O(NlogN) for문은 O(N), str이 O(logN)
def solution(n):
    ret = 0
    for i in range(1, n+1):
        ret += len(str(i))
    return ret

def solution(n):
    return sum(map(lamda x : len(str(x)), range(1, n+1)))

- 더 간단한 풀이: 10씩 나누는 연산이기 때문에 $log_{10}N$으로 가능하다.
  - 수의 길이를 구하는 방법을 생각해보기: 일의 자리 수와 나머지 수로 나누어서 0이 되는 순간 과정을 끝낸다. 

def num_len(n):
    ret = 0
    while n :
        n /= 10
        ret += n
    return ret:

def solution(n):
    l, ret = len(str(n)), 0
    for i in range(1, l):
        ret += i * (10 ** i - 10 ** (i - 1))
        ret += l * (n - 10 ** (l - 1) + 1)
    return ret 

## 안수빈의 팁

### 읽기와 초기화 팁

- 입력의 대표적인 사례: 수, 문자열(문자배열), 배열

num = int(input())

string = input()
chr_lst = list(input())

lst = list(map(int, input().split()))

- map(x, y)는 x함수를  y함수에 모두 적용한 map 객체를 반환한다. char_lst 내용을 문자열로 만들려면, .join을 사용한다.
  
- list 초기화는 comprehension으로 하자. -> set이나 dict도 동일한 방식을 사용할 수 있다. 
lst_1d = [0 for _ in range(N)] # range N만큼 0을 넣은 배열을 만든다.
lst_2d = [[0 for _ in range(N)] for j in range(N)] # N개 만큼 row를 만들고, 그 row를 N개 만큼 만들어라.

### Error case


### 함수의 활용
- case: main함수라고 가정하고 돌리는 경우
- 
ex) 
TC = int(input()) # test case

while TC:
    N, M = map(int, input().split())

    print(answer)
    TC -= 1

- test case를 받고, : 보통은 각각의 내용을 따로 처리해주는 방법이 더 좋다. 감을 잡기 어려움.

ex)
def process()
    N, M = map(int, input().split())

    return answer

for _ in range(int(input())):
    print(process())

- 함수로 무조건 짜는 연습을 하자. 

### 가독성
- 가능한 indent를 줄이는 방법을 수학적인 방법을 사용해서 표현해보자.
- 진수나 진법을 사용할 수 있다. 
  
ex) 
for i in range(N):
    for j in range(N):
        for k in range(N):

은 다음과 같은 방법을 사용해서 줄일 수 있다.

for num in rnage(N**3):
    i, j, k = num // (N*N), num // N % N, num % N

ex)
조건문을 사용할때, 가급적이면 else를 쓰지 않아도 되게 코드를 짜자.
for i in range(N):
    if state:
        process()
는 다음과 같은 방법을 사용하자.
for i in range(N):
    if not state : continue
    process()

def function(x):
    if x:
        return True
    else:
        return False
는 좋지 않다.

def function2(x):
    if x : return True
    return False

def function3(x):
    return True if x else False

### 변수를 사용할때 표기법 통일하기

- 변수에 snake: 소문자만 사용하고, 각 단어 사이에 _ 사용하기
- 함수에 camel: 각 단어의 첫 글자에 대문자를 적지만, 가장 첫 글짜는 소문자를 적는다. 

### 수학

- 주사위 문제의 사례(https://www.acmicpc.net/problem/2484)
- 문제: 같은 눈 확인을 어떻게 하는가? -> 정렬을 통해서 같은 눈을 확인하기: 정렬을 해서 처음이랑 마지막이 같으면 or set을 사용해서 겹치는게 없으면 전부 같은거.

def dice():
    lst = sorted(list(map(int, input().split())))
    if len(set(lst)) == 1:
        return lst[0] * 5000 + 50000
    if len(set(lst)) ==2:
        if lst[1] == lst[2]: return 10000 + lst[1] * 1000
        return 2000 + (lst[1] + lst[2]) * 500
    for i in range(3):
        if lst[i] == lst[i+1]: return 1000 + lst[i] * 100
    return lst[-1] * 100

N = int(input())
print(max(money() for i in range(N)))


