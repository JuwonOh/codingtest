def manhattan_distance(x,y):
    return sum(abs(a-b) for a,b in zip(x,y))
 
def solution(numbers, hand):
    location = {"1": [1,1], "2": [1,2], "3": [1,3], "4": [2,1], "5": [2,2], "6": [2,3],"7": [3,1], "8": [3,2], "9":[3,3], '*':[4,1], '0':[4,2], '#' :[4,3]}
    answer = []
    left_hand = "*"
    right_hand = "#"
    for number in numbers:
        if number in ['1','4','7']:
            answer.append('L')
            left_hand = number
        elif number in ['3', '6', '9']:
            answer.append('R')
            right_hand = number
        else:
            r_distance = manhattan_distance(right_hand[number], location[number])
            l_distance = manhattan_distance(left_hand[number], location[number])
            if r_distance > l_distance:
                answer.append('L')
                left_hand = number
            elif r_distance < l_distance:
                answer.append('R')
                right_hand = number
            else:
                answer.append(hand[0].upper)
    print(answer)
    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"

solution(numbers, hand)