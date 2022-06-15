n = 3

cnt = 0
for h in range(n + 1):
    for m in range(60):
        for s in range(60):
            sum_val = str(h) + str(m) + str(s)
            if "3" in sum_val:
                cnt += 1
            print(sum_val, cnt)
