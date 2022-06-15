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
