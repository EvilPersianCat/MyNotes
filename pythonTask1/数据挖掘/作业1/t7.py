import numpy as np

a = np.array([[1, 2], [3, 4], [5, 6]])
rows, cols = a.shape
print("和", a.sum())
mul = 1
for i in range(rows):
    for j in range(cols):
        mul *= a[i][j]
print("积", mul)
print("平均值", a.mean())
print("最大值", a.max())
print("最大值", a.min())
a[1, 1] = 7
print("元素替换\n", a)
a[1, 1] = 4
print("均值", a.var())
print("标准差", a.std())
