import math
import sys


def func(a, b, c):
    if (b * b - 4 * a * c) < 0:
        print("此方程有两个虚数根")
        x = math.sqrt(-(b * b - 4 * a * c)) / 2 / a
        print(f'{-b}+{x}i')
        print(f'{-b}-{x}i')
        sys.exit()
    elif (b * b - 4 * a * c) == 0:
        print('此方程有一个解')
        return (0 - b + math.sqrt(b * b - 4 * a * c)) / 2 / a
    else:
        print('此方程有两个解')
        return (0 - b + math.sqrt(b * b - 4 * a * c)) / 2 / a, (0 - b - math.sqrt(b * b - 4 * a * c)) / 2 / a


if __name__ == '__main__':
    a = eval(input("请输入系数a："))
    b = eval(input("请输入系数b："))
    c = eval(input("请输入系数c："))
    list1 = func(a, b, c)
    print(list1)
