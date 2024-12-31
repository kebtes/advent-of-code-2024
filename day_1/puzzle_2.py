k = 1000

left_side = []
right_side = []

for _ in range(k):
    l, r = list(map(int, input().split()))

    left_side.append(l)
    right_side.append(r)

from collections import Counter

freq = Counter(right_side)

output = 0

for n in left_side:
    output += (n * freq[n])

print(output)