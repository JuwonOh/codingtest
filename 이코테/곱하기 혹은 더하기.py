string = "02894"
a_list = sorted([num for num in string])

sum_all = 0

for num in a_list:
    num = int(num)
    if num <= 1:
        continue
    elif sum_all <= 1:
        sum_all += num
    else:
        sum_all *= num
print(sum_all)
# 실수한 부분: 1이하를 더하지 않고, 곱한 부분.

# 더 간단한 방법
# sting을 하면 처음 들어가는 0을 없앨 수 있다.

result = int(string[0])

for i in range(1, len(a_list)):
    num = int(a_list[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
