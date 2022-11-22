import math
import numpy as np
from matplotlib.pyplot import *

x = np.linspace(-np.pi, np.pi, 200)
y = np.sin(np.tan(x)) - np.tan(np.sin(x))
plot(x, y)
grid()
show()
