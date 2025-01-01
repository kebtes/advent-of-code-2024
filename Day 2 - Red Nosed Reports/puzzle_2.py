K = 1000

def func(arr):
    n = len(arr)
    for i in range(1, n):
        if arr[i] <= arr[i - 1] or abs(arr[i] - arr[i - 1]) not in (1, 2, 3):
            return False
    return True

output = 0
for _ in range(K):
    try:
        rep = list(map(int, input().split()))
        
        if func(rep) or func(rep[::-1]):
            output += 1
            continue  
        
        is_valid = False
        for i in range(len(rep)):
            new_rep = rep[:i] + rep[i + 1:]
            if func(new_rep) or func(new_rep[::-1]):
                is_valid = True
                break
                
        if is_valid:
            output += 1
            
    except Exception:
        break

print(output)