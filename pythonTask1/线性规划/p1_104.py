# 导入包
from scipy import optimize
import numpy as np

# 确定c,A,b,Aeq,beq
c = np.array([10, 15, 5, 60, 8])
A = np.array([[-0.3, -1.2, -0.7, -3.5, -5.5],
              [-73, -96, -20253, -890, -279],
              [-9.6, -7, -19, -57, -22]])
b = np.array([-50, -4000, -1000])

# 求解
res = optimize.linprog(c, A, b)
print(res)
