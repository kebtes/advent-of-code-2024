K = 1000

def func(arr):
    n = len(arr)

    for i in range(1, n):
        if arr[i] <= arr[i - 1] or abs(arr[i] - arr[i - 1]) not in (1, 2, 3):
            return False
        
    return True
            
reports = []

for _ in range(K):
    reports.append(list(map(int, input().split())))

mon_safe_levels = 0

for i, r in enumerate(reports):
    if func(r) or func(list(reversed(r))):
        mon_safe_levels += 1

print(mon_safe_levels)