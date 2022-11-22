def print_info(x):
    i = max(x)
    j = min(x)
    l = len(x)
    print("最大值=%s" % i,end=",")
    print("最小值=%s" % j,end=",")
    print("元素个数={0}".format(l))
    return i, j, l


s1 = [9, 8, 7, 3, 2, 1, 55, 6]
s2 = ['apple', 'pear', 'melon', 'kiwi']
s3 = 'TheQuickBrownFox'
print("list=%s" % s1)
q = print_info(s1)
print("list=%s" % s2)
w = print_info(s2)
print("list=%s" % s3)
e = print_info(s3)