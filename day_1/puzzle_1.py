def func(left_list, right_list):
    left_list.sort()
    right_list.sort()
    
    total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))
    
    return total_distance

left_list = []
right_list = []

k = 1000

for _ in range(k):
    left, right = list(map(int, input().split()))
    left_list.append(left)
    right_list.append(right)

result = func(left_list, right_list)
print(result)
