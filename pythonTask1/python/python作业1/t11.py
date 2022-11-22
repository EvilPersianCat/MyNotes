import math

x = int(input('请输入'))
if x >= 0:
    y = (x * x - 3 * x) / (x + 1) + 2 * math.pi + math.sin(x)
else:
    y = math.log(-5 * x, math.e) + 6 * math.sqrt(math.fabs(x) + math.e ** 4) - (x + 1) ** 3
print(f'方法一：{y}')

if x >= 0:
    y = (x * x - 3 * x) / (x + 1) + 2 * math.pi + math.sin(x)
if x < 0:
    y = math.log(-5 * x, math.e) + 6 * math.sqrt(math.fabs(x) + math.e ** 4) - (x + 1) ** 3
print(f'方法二：{y}')

if x >= 0:
    y = (x * x - 3 * x) / (x + 1) + 2 * math.pi + math.sin(x)
elif x < 0:
    y = math.log(-5 * x, math.e) + 6 * math.sqrt(math.fabs(x) + math.e ** 4) - (x + 1) ** 3
print(f'方法三：{y}')
