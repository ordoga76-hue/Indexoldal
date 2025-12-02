import sys

s = sys.stdin.readline().strip()
n = len(s)

freq = [0] * 26
for ch in s:
    freq[ord(ch) - 65] += 1

if max(freq) > (n + 1) // 2:
    print(-1)
    sys.exit(0)

res = []
prev = -1

for pos in range(n):
    placed = False
    for c in range(26):
        if freq[c] == 0 or c == prev:
            continue
        freq[c] -= 1
        rem = n - pos - 1
        if max(freq) <= (rem + 1) // 2:
            res.append(chr(c + 65))
            prev = c
            placed = True
            break
        freq[c] += 1
    if not placed:
        print(-1)
        sys.exit(0)

print("".join(res))
