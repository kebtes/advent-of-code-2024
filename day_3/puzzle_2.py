import re

with open("day_3/input.txt", "r") as file:
    memory = file.read()

output = 0

calculate = True
for match in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)", memory):
    print(match.group())
    if match.group(0) == "do()":
        calculate = True
    elif match.group(0) == "don't()":
        calculate = False
    elif match.group(0).startswith("mul"):
        x, y = int(match.group(1)), int(match.group(2))
        if calculate:
            output += x * y

print(output)