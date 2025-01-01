with open("Day 7 - Bridge Repair/input.txt") as file:
    test = file.read().splitlines()

ops = {
    "*": lambda x, y: int(x) * int(y),
    "+": lambda x, y: int(x) + int(y)
}

def evaluate(exp):
    nums = []
    op = ""

    for tk in exp:
        if isinstance(tk, int):
            if nums: nums.append(op(nums.pop(), tk))
            else: nums.append(tk)
        else:
            if tk == "+": op = lambda x, y: x + y
            elif tk == "*": op = lambda x, y: x * y
        
    return nums[-1]

output = 0
def backtrack(path, idx, n, target, num):
    if idx == n:
        # print(path)
        exp = list(map(str, path))
        exp = "".join(exp)

        if evaluate(path) == target: return True
        return False
    
    for op in ops:
        path.append(op)
        path.append(num[idx])

        if backtrack(path, idx + 1, n, target, num): return True

        path.pop()
        path.pop()

    return False

output = 0
count = 0
total = len(test)
for eq in test:
    count += 1
    res, e = eq.split(":")
    e = list(map(int, e.split()))
    if backtrack([e[0]], 1, len(e), int(res), e): output += int(res)
    print(f"Completed: {count/total * 100}")

print(output)




