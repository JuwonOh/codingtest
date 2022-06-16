def solution(nums):
    specifies = len(set(nums))
    selection = len(nums)//2

    if specifies > selection:
        answer = selection
    else:
        answer = specifies
    return answer
