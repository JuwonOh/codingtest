import sys
sys.stdin = open("inflearn/mysolution/input.txt", "rt")
cards = [card for card in range(1, 21)]

for i in range(10):
    s, e = map(int, input().split())
    change = cards[s-1:e:][::-1]
    cards = cards[:s-1] + change + cards[e:]
    print(cards)


# 다른 풀이방법

for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e-s)):
        cards[s+i], cards[e-i] = cards[e-i], cards[s+i]

print(cards)
