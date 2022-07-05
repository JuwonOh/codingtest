##https://school.programmers.co.kr/learn/courses/30/lessons/42883
## https://www.notion.so/95eac0a5d0b241adb462c11b9a0bc034

def solution(number, k):
    res = []
    for num in number:
        
        while res and res[-1] < num and k <0:
            res.pop()
            k -= 1
        res.append(num)
    answer = "".join(res)
    return answer[:len(answer)-k]


### ㄷㅓ ㅇㅏㄴㅈㅗㅎㅇㅡㄴ ㅍㅜㄹㅇㅣ
def solution(number, k):
    a_list = []
    for num in number:
        if k > 0:
            while a_list and a_list[-1] < num:
                a_list.pop()
                k -= 1
                print(a_list, k)
                if k == 0:
                    break
        a_list.append(num)
    
    answer = ''.join(a_list)
    print(answer)
    return answer

