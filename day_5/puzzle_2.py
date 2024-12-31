from collections import defaultdict, deque

with open("day_5/page_x_y.txt", "r") as file:
    page_x_y = file.read().splitlines()

with open("day_5/given_order.txt", "r") as file:
    given_order = file.read().splitlines()

graph = defaultdict(list)
# in_degree = defaultdict(int)

for line in page_x_y:
    x, y = map(int, line.split('|'))
    graph[y].append(x)
    # in_degree[y] += 1
    # in_degree[x] += 0


def check(arr):
    s = set(arr)

    for node in arr:
        s.discard(node)

        for d in graph[node]:
            if d in s:
                return False
            
    return True


def ts(arr):
    sub_graph = {node: [] for node in arr}
    sub_in_degree = {node: 0 for node in arr}

    for node in arr:
        for neighbor in graph[node]:
            if neighbor in sub_graph:
                sub_graph[node].append(neighbor)
                sub_in_degree[neighbor] += 1


    queue = deque([node for node in arr if sub_in_degree[node] == 0])
    output = []

    while queue:
        node = queue.popleft()
        
        output.append(node)

        for neighbor in sub_graph[node]:
            sub_in_degree[neighbor] -= 1

            if sub_in_degree[neighbor] == 0:
                queue.append(neighbor)

    return output

output = 0
for order in given_order:
    o = list(map(int, order.split(",")))
    if not check(o):
        print(o)
        o = ts(o)
        output += (o[len(o) // 2])
    
print(output)