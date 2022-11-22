'''
矩阵连乘问题
A1 A2 A3 A4 A5 A6...相乘，求计算量最小的加括号的方式
m[i][j] :A[i]到A[j]的计算量
s[i][j] :A[i]到A[j] 应该加括号的地方
'''


def MatrixChain(p, n, m, s):
    for r in range(2, n + 1):
        for i in range(1, n - r + 2):
            j = i + r - 1
            m[i][j] = m[i + 1][j] + p[i - 1] * p[i] * p[j]  # 计算m[i][j]
            s[i][j] = i  # 计算s[i][j]
            for k in range(i, j):  # 把计算量大的m替换掉
                t = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if t < m[i][j]:
                    m[i][j] = t
                    s[i][j] = k
    return m[1][n]


def Traceback(i, j, s):
    if i == j:
        print('A%d' % (i), end='')
        return  # i==j 时输出Ai
    print("(", end='')  # 输出左括号，调用递归，输出右括号
    Traceback(i, s[i][j], s)
    Traceback(s[i][j] + 1, j, s)
    print(")", end='')


p = input().split()
n = len(p)
p = [int(x) for x in p]  # 输入A1的行数和列数以及A2,A3...的列数
m = []
s = []
for i in range(n):
    m.append([])
    s.append([])
    for j in range(n):
        m[i].append(0)
        s[i].append(0)  # 初始化m, s
ans = MatrixChain(p, n - 1, m, s)
Traceback(1, n - 1, s)
print('\n最小计算量为：', ans)
