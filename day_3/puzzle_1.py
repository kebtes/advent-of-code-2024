import re

with open('day_3/input.txt', 'r') as file:
    memory = file.read()
    
matches = re.findall("mul\((\d+),(\d+)\)", memory)
total = sum(int(x) * int(y) for x, y in matches)

print(total)
