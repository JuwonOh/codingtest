n = 5
mem_list = sorted([2, 1, 2, 2, 3, 4, 5, 2, 1, 3, 4, 5, 6, ])

group = 0
sum_val = 0
for i in mem_list:
    sum_val += 1
    if sum_val > i:
        group += 1
        sum_val = i
    print(group, sum_val, i)
