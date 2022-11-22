import numpy as np
from matplotlib import pyplot as plt

fig = plt.figure(figsize=(9, 6),
                 facecolor='khaki'
                 )
ax = fig.gca(projection='3d')

# 二元函数定义域平面集
x = np.linspace(start=-300,
                stop=300,
                num=100
                )
y = np.linspace(start=-300,
                stop=300,
                num=100
                )
X, Y = np.meshgrid(x, y)  # 网格数据
Z = (np.power(X, 2) + np.power(Y, 2))/562 - 300  # 二元函数 z = x**2 + y**2

# 绘图
surf = ax.plot_surface(X=X,
                       Y=Y,
                       Z=Z,
                       rstride=2,  # row stride, 行跨度
                       cstride=2,  # column stride, 列跨度
                       color='r',
                       linewidth=0.5,
                       )

# 调整视角
ax.view_init(elev=7,  # 仰角
             azim=30  # 方位角
             )

# 显示图形
plt.show()
