import sympy
from sympy import symbols, plot_implicit

x, y = symbols('x y')#创建两个变量x和y
plot_implicit((x**2+y**2-1)**3-x**2*y**3,(x,-5,5))
#plot_implicit中的第一个参数即为所要绘制的方程，方程右边等于0
#在sympy.log(x,sympy.E)中，sympy.E为自然对数的底