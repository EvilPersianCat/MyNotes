import numpy as np

s = str(input('请输入s'))
lst = list(map(str, input('请输入wordDict').split()))
wordDict = set(lst)
n = len(s)

dp = np.zeros((n, n))
for i in range(0, n):
    for j in range(i, n):
        if s[i:j+1] in wordDict:
            dp[i][j] = 1

for r in range(2, n + 1):
    for i in range(0, n - r + 1):
        j = i + r - 1
        for k in range(i, j):
            if dp[i, k] == 1 and dp[k + 1, j] == 1:
                dp[i, j] = 1
if dp[0, n - 1] == 1:
    print('true')
else:
    print('false')
