import numpy as np
import matplotlib.pyplot as plt

x = [10, 20, 30, 40, 50, 60, 70, 80]
x = np.array(x)
print('x is :\n', x)
num = [174, 236, 305, 334, 349, 351, 342, 323]
y = np.array(num)
print('y is :\n', y)
# f1 为各项的系数，3 表示想要拟合的最高次项是多少。
f1 = np.polyfit(x, y, 3)
# p1 为拟合的多项式表达式
p1 = np.poly1d(f1)
print('p1 is :\n', p1)

plt.plot(x, y, 's', label='original values')
yvals = p1(x)  # 拟合y值
plt.plot(x, yvals, 'r', label='polyfit values')
plt.show()
