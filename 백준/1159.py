# https://www.acmicpc.net/problem/1159

n = int(input())
n_list = [input()[0] for _ in range(n)]
first_name_list = set(n_list)
res = []
for first_name in first_name_list:
    if n_list.count(first_name) >= 5:
        res.append(first_name)
print(''.join(sorted(res)) if len(res) > 0 else "PREDAJA")
