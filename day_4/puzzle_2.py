with open("day_4/input.txt", "r") as f:
    board = f.read().splitlines()

ROW = len(board)
COL = len(board[0])

output = 0
for r in range(1, ROW-1):
    for c in range(1, COL-1):
        if board[r][c] != "A":
            continue

        ul = board[r-1][c-1]
        ur = board[r-1][c+1]
        dl = board[r+1][c-1]
        dr = board[r+1][c+1]

        if sorted([ul, ur, dl, dr]) == ["M", "M", "S", "S"] and ul != dr:
            output += 1
        
print(output)