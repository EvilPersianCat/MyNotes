N = 12
M = N << 12
dp = [[0] * M for _ in range(N)]    #表示每一列，矩阵突出和不突出的状态
tf = [False] * M

def f( x, n, tf ):  # 判断是否存在奇数个连续的0
    cnt = 0
    tf[x] = True
    for t in range(n):
        if x >> t & 1:
            if cnt & 1:
                tf[x] = False
        else:
            cnt += 1
    if cnt & 1:
        tf[i] = False


while( True ):
    n, m = map(int, input().split())
    if n == 0 and m == 0:   # n 行 ， m列
        break
    dp[0][0] = 1
    for i in range( 1 << n ):
        f(i, n, tf)

    for i in range(1, m+1):
        for j in range(1 << n):
            for k in range(1 << n):
                if j & k == 0 and tf[ j | k ]:
                    dp[i][j] += dp[i-1][k]
    print( dp[m][0] )




