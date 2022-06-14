n = 5
plans = ["L", "L", "R", "D", "D"]

x, y = 1, 1

directions = ["R", "L", "U", "D"]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for plan in plans:
    for d_idx in range(len(directions)):
        if plan == directions[d_idx]:
            nx = x + dx[d_idx]
            ny = y + dy[d_idx]
    if nx <= 0 or ny <= 0 or nx > n or ny > n:
        continue  # continue의 용도를 알아두기.
    x = nx
    y = ny
    print(x, y)
