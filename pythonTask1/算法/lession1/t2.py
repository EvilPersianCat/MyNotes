def fun(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fun(n - 1) + fun(n - 2)


x = int(input())
print(fun(x))
