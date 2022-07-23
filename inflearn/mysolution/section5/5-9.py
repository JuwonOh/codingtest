import sys
sys.stdin = open("inflearn/mysolution/input.txt", "rt")

word_list = input()
word_dict = {}
check_list = input()
check_dict = {}

for key in word_list:
    word_dict[key] = word_dict.get(key, 0) + 1

for key in check_list:
    check_dict[key] = check_dict.get(key, 0) + 1

print(check_dict == word_dict)

for i in word_dict.keys():
    print(i, word_dict[i],  check_dict[i])
    if word_dict[i] != check_dict[i]:
        print("No same")
        break
else:
    print("same")
