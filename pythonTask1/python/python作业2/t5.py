s = [9, 7, 8, 3, 2, 1, 5, 6]
print("变换前：", end='')
print(s)
for i in range(0, len(s)):
    if s[i] % 2 == 0:
        s[i] = s[i] * s[i]
print("变换后：", end='')
print(s)
