import numpy as np
import matplotlib.pyplot as plt

x_value = np.random.randint(140, 180, 200)

plt.hist(x_value, bins=10)

plt.title("data")
plt.xlabel("x")
plt.ylabel("y")

plt.show()
