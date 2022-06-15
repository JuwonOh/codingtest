input_knight = ('b4')

row = int(input_knight[1])
col = ord(input_knight[0])
print(col)
directions = [(2, 1), (2, -1), (-2, 1), (-2, -1),
              (1, 2), (1, -2), (-1, 2), (-1, -2)]
cnt = 0
for direction in directions:
    c_r = row + direction[0]
    c_c = col + direction[1]

    if c_r >= 1 and c_r <= 8 and c_c >= int(ord("a")) and c_c <= int(ord("i")):
        cnt += 1

    print(c_r, c_c, cnt)
