def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

f = []
n = int(input())
for i in range(1,n+1):
    res = fib(i)
    print( '{num:5}'.format(num=res),end="" )
    if i % 10 == 0:
        print()
    





