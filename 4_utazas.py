import sys

data = list(map(int, sys.stdin.read().split()))
n = data[0]
a = data[1:]

last_pos = [-1] * (n + 1)
start = 0
best = 0

for i, city in enumerate(a):
    if last_pos[city] >= start:
        start = last_pos[city] + 1
    last_pos[city] = i
    length = i - start + 1
    if length > best:
        best = length

print(best)
