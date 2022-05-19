def solution(new_id):
    ##1단계
    new_id = new_id.lower()
    ## 2단계
    answer = ''
    for word in new_id:
        if word.isalnum() or word in "-_.":
            answer += word
    ## 3단계
    while ".." in answer:
        answer = answer.replace("..", ".")
    ## 4단계
    answer = answer[1:] if answer[0] == "." and len(answer) > 1 else answer
    answer = answer[:-1] if answer[-1] == "." else answer
    ## 5단계
    answer = "a" if len(answer) == 0 else answer   
    ## 6단계
    answer = answer[:15] if len(answer) >= 16 else answer
    answer = answer[:-1] if answer[-1] == "." else answer
    ## 7단계
    if len(answer) <3:
        answer = answer + answer[-1] * (3- len(answer))
    
    return answer

## 정규식을 사용해서 풀어보기

import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = "a" if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st + st[-1] * (3- len(st)) if len(st) <3  else st 
    
    return st