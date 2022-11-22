import math
import numpy as np
from matplotlib.pyplot import *

x = np.linspace(-np.pi, np.pi, 200)
interval1 = [1 if (i > 1 or i < -1) else 0 for i in x]
interval2 = [1 if (1 >= i >= -1) else 0 for i in x]
y1 = 1.1*np.sin(x)*interval1+x*interval2
y2 = (np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))
plot(x, y1)
plot(x, y2, linestyle='dotted')
grid()
show()
