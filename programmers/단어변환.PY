def check(word1, word2):
    cnt = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            cnt += 1
    return cnt


def solution(begin, target, words):
    temp = []
    if target not in words:
        return 0

    def dfs(index, b_word):
        if target not in words or index == len(words):
            return 0
        else:
            if check(words[index], b_word) == 1:
                b_word = words[index]
                temp.append(words[index])
                print(words[index], b_word)
                dfs(index + 1, b_word)
            else:
                dfs(index + 1, b_word)
    dfs(0, begin)
    
    
    

    return len(temp)


## dfs를 사용한 다른 풀이

num_list = []
def solution(begin, target, words):
    answer = 0
    if target not in words:
        return answer
    words.append(begin)
    
    visited = {}
    for i in words:
        visited[i] = False
    
    node_dic = {}
    
    for i in words:
        node_dic[i] = []
    
    for i in words:
        for j in words:
            if check(i, j) == 1:
                node_dic[i].append(j)
    dfs(begin, target, node_dic, visited, 0)
    return min(num_list)
    
def dfs(start, target, node_dic, visited, num):
    visited[start] = True
    
    if start == target:
        num_list.append(num)
        return
    
    for i in node_dic[start]:
        if visited[i] == False:
            dfs(i, target, node_dic, visited, num+1)
            visited[i] = False
    
