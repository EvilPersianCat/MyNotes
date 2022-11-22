# n个整数全排列
import numpy as np


def Perm(arr, start, size):
    # 定义递归结束的条件，也是打印当前排列
    if start == size:
        print(arr)
    else:
        # 对数组（start，end）部分第一位元素所有可能进行遍历
        for index in range(start, size):
            # 交换第一个元素和数组（start，end）部分的另一个元素
            arr[index], arr[start] = arr[start], arr[index]
            # 递归，对确定下一位元素
            Perm(arr, start + 1, size)
            # 将数组恢复成交换之前
            arr[index], arr[start] = arr[start], arr[index]


def main():
    # 用numpy来对数组进行操作，下方代码为接收一个类型为int型的数组；
    # split()方法：通过指定分隔符对接收的字符串进行切片；
    arr = np.array(input().split(), dtype=int)
    # 调用Perm函数对数组进行全排列
    # arr.size 求出ndarray数组中元素的数量
    Perm(arr, 0, arr.size)


if __name__ == '__main__':
    main()



