def f(list):
    resultList = []
    for item in list:
        if not item in resultList:
            resultList.append(item)
    return resultList


lst = list(map(str, input().split()))
ans = f(lst)
print(ans)
