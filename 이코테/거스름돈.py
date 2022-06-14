N = 1260
money = [500, 100, 50, 10]

cnt = 0

for i in money:
    cnt += N//i
    N %= i
print(cnt)

# 주의: 변수를 다룰 때 너무 복잡하게 생각하지 말자.
