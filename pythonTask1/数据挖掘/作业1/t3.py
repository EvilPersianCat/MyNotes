import numpy as np

a = np.random.random((3, 2))
a = a.reshape(-1, 1)
print(a[-1])
print()

b = a[1:4]
print(b)
print()

length = len(a)
for i in range(0, length):
    print(a[length-i-1], end="")
