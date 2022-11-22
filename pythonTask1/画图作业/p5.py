from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

figure = plt.figure()
ax = Axes3D(figure)
X = np.arange(-3, 2, 0.08)
Y = np.arange(-2, 2, 0.08)
X, Y = np.meshgrid(X, Y)
Z = (X**2-2**X)*np.exp(-X**2-Y**2-X*Y)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
plt.show()
