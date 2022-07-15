import sys
sys.stdin = open("inflearn/mysolution/input.txt", "rt")


n = int(input())
boxs = list(map(int, input().split()))
change = int(input())


while change != 0:
    smallest = max(boxs)
    largest = 0
    for idx in range(len(boxs)):
        if boxs[idx] > largest:
            largest = boxs[idx]
            large_idx = idx
        if boxs[idx] < smallest:
            smallest = boxs[idx]
            small_idx = idx
    boxs[large_idx] -= 1
    boxs[small_idx] += 1
    change -= 1
print(max(boxs)-min(boxs))


# 그리디한 해법
sys.stdin = open("inflearn/mysolution/input.txt", "rt")

n = int(input())
boxs = list(map(int, input().split()))
change = int(input())

boxs.sort()
for _ in range(change):
    boxs[0] += 1
    boxs[n-1] -= 1
    boxs.sort()

print(max(boxs)-min(boxs))
