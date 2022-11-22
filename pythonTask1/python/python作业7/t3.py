from calendar import *

def ndays(y,m):

    monthDays=[31,28,31,30,31,30,31,31,30,31,30,31]

    days = monthDays[ m-1 ]

    if(m==2 and isleap(y)):

        days+=1

    return(days)

def caldays(y,m,d):

    nleaps = 0

    nonleaps = 0

    monthDay = 0

    for i in range(1,y):

        if isleap(i):

            nleaps +=1

        else:

            nonleaps+=1

    yearDay=nonleaps*365+nleaps*366

    for i in range(1,m):

        monthDay += ndays(y,i)

    dayDay = d

    return yearDay +monthDay +dayDay     

#测试代码

y=int(input("请输入年份（>=1）,否则为1："))

m=int(input("请输入月份（1--12），否则<1为1，>12为12："))

d=int(input("请输入天数（1--31），否则<1为1，>31为31："))

if y<1:y=1

if m<1:m=1

if m>12:m=12

if d<1:d=1

if d>31:d=31

print("{0} 年 {1} 月 {2} 日是星期 {3}".format(y,m,d,caldays(y,m,d)%7))