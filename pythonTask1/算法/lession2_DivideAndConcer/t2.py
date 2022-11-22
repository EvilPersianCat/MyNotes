# 最大连续字段和
import numpy as np


def fun(arr, left, right):
    ans = 0
    while right < arr.size:
        right += 1
        curs = 0
        for i in range(left, right):
            curs += arr[i]
        if curs < 0:
            left = right
        ans = max(ans, curs)
    print(ans)


def main():
    arr = np.array(input().split(), dtype=int)
    fun(arr, 0, 0)


if __name__ == '__main__':
    main()
