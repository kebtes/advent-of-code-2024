with open("day_4/input.txt", "r") as f:
    content = f.read().splitlines()

ROW = len(content)
COL = len(content[0])

directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

match = "XMAS"
output = 0

def check_direction(x, y, dx, dy):
    for i in range(len(match)):
        nx, ny = x + i * dx, y + i * dy
        if not (0 <= nx < ROW and 0 <= ny < COL and content[nx][ny] == match[i]):
            return False
    return True

for r in range(ROW):
    for c in range(COL):
        if content[r][c] == match[0]:  
            for dx, dy in directions:
                if check_direction(r, c, dx, dy):
                    output += 1

print(output)
