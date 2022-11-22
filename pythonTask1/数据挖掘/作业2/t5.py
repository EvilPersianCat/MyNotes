import matplotlib
import matplotlib.pyplot as plt
import numpy as np

N = 100
x = np.random.rand(N)
y = np.random.rand(N)
s = (30*np.random.rand(N))**2
c = np.random.rand(N)
plt.scatter(x, y, s=s, c=c, alpha=0.5)
plt.show()
