# 归并排序


def mergesort(lst):
    n = len(lst)
    if n < 2:
        return lst
    mid = n // 2
    left = lst[:mid]
    right = lst[mid:]

    left_sort = mergesort(left)
    right_sort = mergesort(right)

    res = merge(left_sort, right_sort)
    return res


def merge(left, right):
    global ans
    res = []
    while left and right:
        if left[0] <= right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
            ans += len(left)
    if left:
        res.extend(left)
    if right:
        res.extend(right)

    return res


def main():
    # global ans
    lst = list(map(int, input().split(',')))
    lst = mergesort(lst)
    print(lst)
    print(ans)


if __name__ == '__main__':
    ans = 0
    main()
