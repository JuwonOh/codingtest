
## dict와 isalpha를 사용한 solution
def solution(s):
    dict = {}
    en = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    alpha_to_num = ""
    each_num = ''
    for idx, num in enumerate(en):
        dict[num] = idx
    for i in s:
        if i.isdigit():
            each_num += i
        if i.isalpha():
            alpha_to_num += i
            if alpha_to_num in dict.keys():
                each_num += str(dict[alpha_to_num])
                alpha_to_num = ''
    return int(each_num)
    
    
## if와 replace를 사용한 방법

def solution(s):
    en = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    answer = ''
    for idx, num in enumerate(en):
        if num in s:
            s.replace(num, idx)
    return s
    
    