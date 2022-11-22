import numpy as np
from matplotlib import pyplot as plt

fig = plt.figure()
ax1 = plt.axes(projection='3d')

t = np.linspace(0, 2*np.pi, 1000)
x = t**3*np.exp(-t)*np.sin(3*t)
y = t**3*np.exp(-t)*np.cos(3*t)
z = t**2

ax1.plot3D(x, y, z, 'gray')  # 绘制空间曲线
plt.show()
