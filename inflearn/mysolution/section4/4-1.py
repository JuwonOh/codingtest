import sys
sys.stdin = open("inflearn/mysolution/input.txt", "rt")

length, value = map(int, input().split())

num_list = sorted(list(map(int, input().split())))

s = 0
e = length-1


while s < e:
    mid = abs((e+s) // 2)-1
    if num_list[mid] == value:
        print(num_list[mid], value, mid+1)
        break
    elif num_list[mid] < value:
        s = abs(mid-1)
    else:
        e = abs(mid + 1)
