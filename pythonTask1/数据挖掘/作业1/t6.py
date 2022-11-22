import numpy as np

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[2, 1], [4, 5]])

print("arr1\n", arr1)
print("arr2\n", arr2)
print("加：\n", arr1 + arr2)
print("减：\n", arr1 - arr2)
print("乘：\n", arr1 * arr2)
print("除：\n", arr1 / arr2)
print("相等：\n", (arr1 == arr2).all())
