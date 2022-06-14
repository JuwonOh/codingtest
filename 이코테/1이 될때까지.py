n = 25
k = 4
cnt = 0

while n != 0:
    if n % k != 0:
        n = n - 1
        cnt += 1
    else:
        n = n//k
        cnt += 1
    print(cnt, n)

# 다른 방법- 더 빠른 방법 log 시간 복잡도

res = 0

while True:
    # for문을 사용하지 않아도, k로 나누어 떨어지는 양만 남긴다.
    target = (n//k)*k
    res += n - target
    # 나머지를 등록한다.
    n = target
    # 더이상 나누어 떨어지지 않는지 확인한다.
    if n < k:
        break
    # k로 나누어 떨어지면 기록한다.
    res += 1
    n //= k

res += (n-1)
print(res)
