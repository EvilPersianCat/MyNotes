def fact1(n):
    if n == 1 :
        return 1
    else:
        return n*fact1(n-1)

def fact2(n):
    res = 1;
    while(n != 1):
        res = res * n
        n = n-1
    return res

x = int(input('请输入整数n:'))
print(fact1(x))
print(fact2(x))