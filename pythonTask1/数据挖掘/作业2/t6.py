import numpy as np
import matplotlib.pyplot as plt

np.random.seed(10)
collectn_1 = np.random.normal(100, 10, 200)
collectn_2 = np.random.normal(80, 30, 200)
collectn_3 = np.random.normal(90, 20, 200)
collectn_4 = np.random.normal(70, 25, 200)
data_to_plot = [collectn_1, collectn_2, collectn_3, collectn_4]

plt.boxplot(data_to_plot, notch=False, sym='rs', vert=True)
plt.xticks([y + 1 for y in range(len(data_to_plot))], ['x1', 'x2', 'x3', 'x4'])
plt.xlabel('x')
t = plt.title('plot')
plt.show()
