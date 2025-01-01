with open("day_6/input.txt", "r") as file:
    board = file.read().splitlines()

ROW = len(board)
COL = len(board[0])

guard = None

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
direction_idx = 0

for r in range(ROW):
    for c in range(COL):
        if board[r][c] in "><^V":
            if board[r][c] == ">": direction_idx = 0
            elif board[r][c] == "V": direction_idx = 1
            elif board[r][c] == "<": direction_idx = 2
            else: direction_idx = 3

            guard = (r, c)

seen = set()
i, j = guard
for _ in range(ROW * COL):
    seen.add((i, j))

    ni, nj = i + direction[direction_idx][0], j + direction[direction_idx][1]

    if not (0 <= ni < ROW and 0 <= nj < COL):
        break

    if board[ni][nj] == "#":
        direction_idx = (direction_idx + 1) % 4
        ni, nj = i + direction[direction_idx][0], j + direction[direction_idx][1]
    
    i, j = ni, nj

print(len(seen))