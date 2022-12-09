def f():
    print("请输入字符串：")
    lst = list(map(str, input().split()))
    print("字符串的个数：")
    print(len(lst))


if __name__ == "__main__":
    f()
