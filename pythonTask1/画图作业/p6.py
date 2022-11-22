from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

xlist = np.linspace(-2.0, 1.0, 100)  # Create 1-D arrays for x,y dimensions
ylist = np.linspace(-1.0, 2.0, 100)
X, Y = np.meshgrid(xlist, ylist)  # 计算圆所在区域的网格
Z = np.sqrt(X ** 2 + Y ** 2)  # 计算结果
plt.contour(X, Y, Z, [0.5, 1.0, 1.2, 1.5])  # [0.5, 1.0, 1.2, 1.5] 指明方程右面的值
plt.axes().set_aspect('equal')  # 使x,y轴的单位长度一致
plt.axis([-1.0, 1.0, -0.5, 0.5])  # 坐标轴显示范围
plt.show()
