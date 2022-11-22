import math


class MyMath:
    def __init__(self, r):
        self.r = r

    def C(self, r):
        return "%.2f" % (2 * math.pi * self.r)

    def S(self, r):
        return "%.2f" % (math.pi * self.r * self.r)

    def Q_S(self, r):
        return "%.2f" % (4 * math.pi * self.r * self.r)

    def Q_V(self, r):
        return "%.2f" % (4 / 3 * math.pi * math.pow(self.r, 3))


R = float(input("请输入半径:"))
d1 = MyMath(R)
print("圆的周长=", d1.C(R))
print("圆的面积=", d1.S(R))
print("球的表面积=", d1.Q_S(R))
print("球的体积=", d1.Q_V(R))
