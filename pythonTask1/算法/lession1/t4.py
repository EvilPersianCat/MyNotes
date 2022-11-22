import sys


def fun(target, left, right, mlist):
    if left > right:
        print('小于x的最大元素i的位置:', right)
        print('大于x的最小元素j的位置:', left)
        sys.exit()
    mid = int(left + (right - left) / 2)
    if mlist[mid] == target:
        return mid
    elif mlist[mid] > target:
        return fun(target, left, mid - 1, mlist)
    else:
        return fun(target, mid + 1, right, mlist)


n = int(input())
mlist = []
for i in range(0, n):
    x = int(input())
    mlist.append(x)
mlist.sort()
target = int(input())
print(fun(target, 0, n - 1, mlist))
