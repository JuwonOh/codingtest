q = 'a23kfdji43890'

alpha = []
numeric = 0
for i in q:
    if i.isalpha() == True:
        alpha.append(i)
    else:
        numeric += int(i)
alpha.sort()
print(alpha)
if numeric != 0:
    alpha = alpha.extend(str(numeric))

result = ''.join(alpha)
print(result)

def solution(answers):
    a = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    a_cnt, b_cnt, c_cnt = 0
    for i in range(len(answers)):
        if answer[i] == a[i]:
            a_cnt += 1
        elif answer[i] == b[i]:
            b_cnt += 1
        elif answer[i] == c[i]:
            c_cnt += 1
    answer = sorted([a_cnt, b_cnt, c_cnt])
    print(answers)
    return answer
