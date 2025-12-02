s = input().strip()

if not s:
    print(0)
else:
    max_len = 1
    cur = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            cur += 1
            if cur > max_len:
                max_len = cur
        else:
            cur = 1
    print(max_len)
