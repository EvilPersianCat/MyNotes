N = int(input())
matrix = [[0] for _ in range(N+1) ]
for i in range(1, N + 1):
    matrix[i].extend( list( map( int , input().split() ) ) )
# print(matrix)
dp = [[-1e9] * (N + 1) for _ in range(N + 1)]
dp[1][1] = matrix[1][1]
for i in range(2, N + 1):
    for j in range(1, i + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + matrix[i][j]
print(max(dp[-1]))
