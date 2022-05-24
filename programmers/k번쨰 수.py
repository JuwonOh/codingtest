array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array, commands):
    for specific_command in commands:
        print(specific_command.split())
        for i, j, k in specific_command:
            answer.append(array[i-1:j-1].sortd()[k-1])
    
    answer = []
    print(answer)
    return answer

solution(array, commands)