N = int(input())
nums = [0]
nums.extend( list( map( int, input().split() ) ))
dp = [ [1e9] * (N+1) for _ in range(N+1)]  # 初始化时要注意
s = [0] * (N+1)
for i in range(1,N+1):
    s[i] = s[i-1] + nums[i]
    dp[i][i] = 0

for L in range( 2 , N+1 ):
    for i in range( 1, N+1 ):
        j = i + L - 1
        if j >= N+1:
            break
        for k in range( i , j ):
            dp[i][j] = min( dp[i][j] , dp[i][k] + dp[k+1][j] + s[j] - s[i-1] )
print(dp[1][N])