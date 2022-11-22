import math

import numpy as np
3
a = int(input())
b = int(input())
c = int(input())

L = [a, b, c]
a = np.array(L)
a.sort()
if a[0] + a[1] > a[2]:
    print('可以')
    s = sum(a)
    h = s/2
    print(s)
    print(math.sqrt(h*(h-a[0])*(h-a[1])*(h-a[2])))
else:
    print('不可以')
