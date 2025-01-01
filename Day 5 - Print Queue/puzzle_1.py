from collections import defaultdict

with open("day_5/page_x_y.txt", "r") as file:
    page_x_y = file.read().splitlines()

with open("day_5/given_order.txt", "r") as file:
    given_order = file.read().splitlines()

graph = defaultdict(list)
for line in page_x_y:
    x, y = line.split("|")

    graph[int(y)].append(int(x))

def check(arr):
    s = set(arr)

    for node in arr:
        s.discard(node)

        for d in graph[node]:
            if d in s:
                return False
            
    return True

# print(graph)
output = 0
for order in given_order:
    o = list(map(int, order.split(",")))
    if check(o):
        output += (o[len(o) // 2])
    
print(output)