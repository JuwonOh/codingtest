n = 5
plans = ["R", "L", "L", "D", "D", "L"]

x = 1
y = 1

direction = ["R", "L", "U", "D"]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for plan in plans:
    for i in range(len(direction)):
        if direction[i] == plan:
            tmp_x = x + dx[i]
            tmp_y = y + dy[i]
    if tmp_x == 0 or tmp_y == 0:
        x = tmp_x
        y = tmp_y
    print(plan, x, y)
