def judge(year):
    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        return 1
    else:
        return 0


for i in range(2000, 3001):
    if judge(i):
        print(i)
