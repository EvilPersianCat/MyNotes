N = int(input())
nums = list( map(int, input().split()) )
dp = [1] * (N+1) #表示以 i 为结尾的所有子序列中递增且最长的
dp[0] = 0
resp = 0
for i in range( 1, N+1 ):
    for j in range( 1, i ):
        if nums[i-1] > nums[j-1]:  # 严格单调递增
            dp[i] = max(dp[i] , dp[j] + 1)
    resp = max(resp, dp[i])
    # print(resp)
print(resp)
