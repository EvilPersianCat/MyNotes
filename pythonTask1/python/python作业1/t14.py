import math

a = int(input())
b = int(input())

gcd = math.gcd(a, b)
lcd = a * b / gcd
print(f'最大公约数:{gcd}')
print(f'最小公倍数:{lcd}')
