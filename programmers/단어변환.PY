def check(word1, word2):
    cnt = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            cnt += 1
    return cnt


answer = 1


def solution(begin, target, words):
    if target not in words:
        return 0

    def dfs(index, b_word):
        global answer
        if target not in words:
            return 0
        else:
            if check(words[index], b_word) == 1:
                if check(words[index], target) != check(words[index+1], target):
                    b_word = words[index]
                    answer += 1
                    print(words[index], b_word)
                    dfs(index + 1, b_word)
            else:
                dfs(index + 1, b_word)
    dfs(0, begin)

    return answer
